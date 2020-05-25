# covid19-preprocess
Repo for essential preprocessing scripts for the Covid19 simulations

## Obtaining an OSM file.
OSM files are obtained from either Openstreetmaps.org, or using the OSRM tool.

## Extracting locations
You can do this using:
`python3 extract_<location_type>.py <osm_file> > <out_dir>/<location_type>.csv`

## Creating a buildings.csv for FACS
To create a buildings.csv for FACS, simply concatenate all the previously extracted locations into one CSV file.
