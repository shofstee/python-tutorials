import requests


def printdata(response_dict):
    print(response_dict.keys())
    print(f"Total repositories: {response_dict['total_count']}")
    # Explore information about the repositories.
    repo_dicts = response_dict['items']
    print(f"Repositories returned: {len(repo_dicts)}")
    # Examine the first repository.
    repo_dict = repo_dicts[0]
    print(f"\nKeys: {len(repo_dict)}")
    for key in sorted(repo_dict.keys()):
        print(key)

    print("\nSelected information about first repository:")
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")


class GithubRepositoriesPrinter:
    url = 'https://api.github.com/search/repositories?q=language:java&sort=stars'
    headers = {'Accept': 'application/vnd.github.v3+json'}
    status_code = -1

    def get_data(self):
        self.status_code = -1
        r = self.call_api()
        self.status_code = r.status_code
        # Store API response in a variable.
        return r.json()

    def call_api(self):
        return requests.get(self.url, headers=self.headers)


if __name__ == '__main__':
    # Make a game instance, and run the game.
    printer = GithubRepositoriesPrinter()
    data = printer.get_data()
    printdata(data)
