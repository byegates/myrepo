#!/usr/bin/env python

"""
Commandline tool for interacting with library
"""

import click, pandas as pd, pickle
from click import echo

from myrepolib.repomod import print_name
from myrepolib import __version__

def green(s):
    return click.style(s, fg='green')


urls = {
    'cases': 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv',
    'deaths': 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv',
    'recovered': 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv',
    'latest': 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/web-data/data/cases_country.csv',
}

def req_and_save(category):
    url = urls[category]
    echo("")
    echo(f"Retrieving {green(category)} from {green(url)}")
    df = pd.read_csv(url)
    path = f"./data/{category}.df"
    echo(f"Saving retrieved data to {green(path)}")
    pickle.dump(df,open(path, 'wb'))
    return df


@click.version_option(__version__)
@click.command()
@click.option("--category", help="retreive covid19 data from github")
def cli(category):
    """
    retreive covid19 data from github by category
    four valid values: cases, deaths, recovered, latest, all
    cases will retrieve time series data of cases
    deaths will retreve time series data of total number of deaths
    recovered will retrieve time series data of total number of recovered cases
    latest will retreive latest data of all category by country/region
    all will retrieve all types of data
    all data will be saved in pickle format in ./data folder
    """
    if category in urls or category == 'all':
        if category == 'all':
            for category in urls:
                req_and_save(category)
        else:
            req_and_save(category)
    else:
        click.echo(f"{click.style(category, bg='yellow', fg='red')} not valid")


if __name__ == '__main__':
    #pylint: disable=no-value-for-parameter
    cli()
