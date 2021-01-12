import requests
import os

# A simple script for downloading the data from the Marshall Project's public repo

def retrieve(filename):
    # make request
    template_url="https://raw.githubusercontent.com/themarshallproject/COVID_prison_data/master/data/{}"
    resp = requests.get(template_url.format(filename))

    # save file
    with open('folder' + os.sep + filename, 'wb') as f:
        f.write(resp.content)

def main():
    retrieve("covid_prison_cases.csv")
    retrieve("covid_prison_rates.csv")
    retrieve("prison_populations.csv")
    retrieve("staff_populations.csv")

if __name__ == "__main__":
    main()
