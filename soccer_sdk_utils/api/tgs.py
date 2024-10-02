import http.client
import json

from typing import Optional

from abc import ABC, abstractmethod

HOST = "public.totalglobalsports.com"

HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

def fetch_data(host: str, endpoint: str) -> dict[any, any]:
    url = f"https://{host}{endpoint}"
    print(f"Fetching data from: '{url}'")

    try:
        conn = http.client.HTTPSConnection(host)
        conn.request("GET", endpoint, headers=HEADERS)
        response = conn.getresponse()

        if response.status != 200:
            raise http.client.HTTPException(f"HTTP error occurred: {response.status}")

        response_body = response.read()
        conn.close()
    except http.client.HTTPException as e:
        print(f"HTTP error occurred: {e}")
        raise
    except ConnectionError as e:
        print(f"Connection error occurred: {e}")
        raise
    except TimeoutError as e:
        print(f"Timeout error occurred: {e}")
        raise
    except json.JSONDecodeError as e:
        print(f"JSON decode error occurred: {e}")
        raise
    except OSError as e:
        print(f"OS error occurred: {e}")
        raise


    try:
        json_data = json.loads(response_body)
    except json.JSONDecodeError as e:
        print(f"JSON decode error occurred: {e}")
        raise

    return json_data

class AbstractRetriever(ABC):
    @abstractmethod
    def get(self) -> dict[any, any]:
        pass

class StatesRetriever(AbstractRetriever):
    """
    This class is responsible for retrieving states from the TGS API.
    """
    def get(self) -> dict[any, any]:
        json_data = fetch_data(HOST, "/api/Association/get-all-states")
        inner_data = json_data.get("data")

        if inner_data is None:
            raise ValueError("No data found in JSON response")

        return inner_data

class CountriesRetriever(AbstractRetriever):
    """
    This class is responsible for retrieving countries from the TGS API.
    """
    def get(self) -> Optional[list[any]]:
        json_data = fetch_data(HOST, "/api/Association/get-all-countries")
        inner_data = json_data.get("data")

        if inner_data is None:
            raise ValueError("No data found in JSON response")

        return inner_data


class OrganizationsRetriever(AbstractRetriever):
    ecnl_only: bool = False
    organizations_cache: list[any] = None

    """
    This class is responsible for retrieving organizations from the TGS API.
    """
    def __init__(self, ecnl_only: bool = True):
        self.ecnl_only = ecnl_only

    def get(self) -> list[any]:
        if self.organizations_cache is not None:
            return self.organizations_cache

        json_data = fetch_data(HOST, "/api/Association/get-current-orgs-list")
        inner_data = json_data.get("data")

        if inner_data is None:
            raise ValueError("No data found in JSON response")

        if not self.ecnl_only:
            return inner_data

        # Todo: Filter out only ECNL organizations
        self.organizations_cache = []
        for item in inner_data:
            org_name = item.get("orgName")
            if org_name is None:
                continue

            if "ECNL" in org_name:
                self.organizations_cache.append(item)

        return self.organizations_cache

    def get_by_name(self, name: str) -> Optional[dict[any, any]]:
        organizations = self.get()
        for item in organizations:
            org_name = item.get("orgName")
            if org_name is None:
                continue

            if name == org_name:
                return item

        return None

    def get_by_id(self, org_id: int) -> Optional[dict[any, any]]:
        organizations = self.get()
        for item in organizations:
            current_org_id = item.get("orgId")
            if current_org_id is None:
                continue

            if org_id == current_org_id:
                return item

        return None

if __name__ == "__main__":
    states = StatesRetriever().get()
    all_organizations = OrganizationsRetriever(False).get()
    ecnl_organizations = OrganizationsRetriever(True).get()

    print("\nStates:")
    print(json.dumps(states, indent=4))

    print("\nOrganizations:")
    print(json.dumps(all_organizations, indent=4))

    print("\nECNL Organizations:")
    print(json.dumps(ecnl_organizations, indent=4))

    print("\nOrganizations by name:")
    print(json.dumps(OrganizationsRetriever(False).get_by_name("Texas Club Soccer League"), indent=4))

    print("\nOrganizations by ID:")
    print(json.dumps(OrganizationsRetriever(False).get_by_id(23), indent=4))
