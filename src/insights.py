from src.jobs import read


def get_unique_job_types(path):
    jobs_data = read(path)
    jobs_types_unique = []
    for job in jobs_data:
        if job['job_type'] not in jobs_types_unique:
            jobs_types_unique.append(job['job_type'])
    return jobs_types_unique


def filter_by_job_type(jobs, job_type):
    filtered_list = []
    for job in jobs:
        if job['job_type'] == job_type:
            filtered_list.append(job)
    return filtered_list


def get_unique_industries(path):
    jobs_data = read(path)
    industries_unique = []
    for job in jobs_data:
        if job['industry'] not in industries_unique:
            if job['industry'] != '':
                industries_unique.append(job['industry'])
    return industries_unique


def filter_by_industry(jobs, industry):
    filtered_list = []
    for job in jobs:
        if job['industry'] == industry:
            filtered_list.append(job)
    return filtered_list


def get_max_salary(path):
    jobs_data = read(path)
    all_max_salaries = []
    for job in jobs_data:
        if job['max_salary'] not in all_max_salaries:
            if job['max_salary'] != '' and job['max_salary'].isdigit():
                all_max_salaries.append(int(job['max_salary']))
    max_salary = max(all_max_salaries)
    return max_salary
    # pass


def get_min_salary(path):
    jobs_data = read(path)
    all_min_salaries = []
    for job in jobs_data:
        if job['min_salary'] not in all_min_salaries:
            if job['min_salary'] != '' and job['min_salary'].isdigit():
                all_min_salaries.append(int(job['min_salary']))
    min_salary = min(all_min_salaries)
    return min_salary
    # pass


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
