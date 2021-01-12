import requests
import re

# A simple script for downloading the data from the Marshall Project's public repo

def retrieve(dataset_url):
    # make request
    resp = requests.get(dataset_url)

    # save file
    filename = re.search("(?<=/data/).+", dataset_url).group()
    with open(filename, 'wb') as f:
        f.write(resp.content)

def main():
    template_url="https://raw.githubusercontent.com/themarshallproject/COVID_prison_data/master/data/{}"
    retrieve(template_url.format("covid_prison_cases.csv"))
    retrieve(template_url.format("covid_prison_rates.csv"))
    retrieve(template_url.format("prison_populations.csv"))
    retrieve(template_url.format("staff_populations.csv"))

if __name__ == "__main__":
    main()
