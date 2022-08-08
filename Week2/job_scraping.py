# Python Class #2 on web scraping

# Import requests library to do HTTP calls.
import requests

# Send a GET request to Airmar's careers page.
new_data = requests.get("https://www.airmar.com/careers.html").text

# Initialize a list to store job information.
jobs = []

# Set a boolean to monitor for our scraping loop.
job_found = True

while job_found:
    # Attempt to split on HTML tags
    # https://www.w3schools.com/python/ref_string_split.asp
    try:
        # Use split() string method to split out the job title.
        title_start = new_data.split(r'<h4 class="darkBlueColor">', 1)[1]
        title_stop = title_start.split(r"</h4>", 1)
        title = title_stop[0].strip()

        # Use split() sting method to split out the job description.
        description_start = title_stop[1].split(r"<p>", 1)[1]
        description_stop = description_start.split(r"<br />", 1)
        description = description_stop[0].strip()

        # Use split() string method to split out job location.
        location_start = description_stop[1].split(r"<strong>(", 1)[1]
        location_stop = location_start.split(r")</strong>", 1)
        location = location_stop[0].strip()

        # Set new_data to what remains of our string
        new_data = location_stop[1]

        # Build our job info into a dictionary.
        job_info = {"title": title, "description": description, "location": location}

        # Append job into to list of jobs
        jobs.append(job_info)
    # Threw a code trying to parse info, likely out of viable parsing stuff.
    except:
        job_found = False
        pass
print(jobs)
