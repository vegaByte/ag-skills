import subprocess

def git_changelog(repo_path:str, start_date:str, end_date:str):
    """
    Get the changelog for a given repository between specified dates.

    Args:
    repo_path (str): The path to the repository.
    start_date (str): The start date for the changelog. Format is "YYYY-MM-DD"
    end_date (str): The end date for the changelog. Format is "YYYY-MM-DD"

    Returns:
    changelog (str): The changelog for the repository between the specified dates.
    """

    git_log_command = f'git log --since="{start_date}" --until="{end_date}"'

    try:
        changelog = subprocess.check_output(git_log_command, shell=True, cwd=repo_path, text=True)
        print(changelog)
        return changelog
    except subprocess.CalledProcessError as e:
        print(f'An error occurred while trying to get the changelog: {e}')
