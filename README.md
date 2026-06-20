# ETL Pipeline Project

## Overview

This repository contains an ETL pipeline for extracting, transforming, and loading data into a PostgreSQL database. The pipeline is designed to be run locally and can be configured using environment variables.

## Requirements

Install the required Python packages from `requirements.txt` using pip.

```powershell
pip install -r requirements.txt
```

## Environment Setup

Set the following PostgreSQL environment variables before running the pipeline. Make sure you replace the variables relative to your database 

### Windows (PowerShell)

```powershell
$env:POSTGRES_HOST = 'localhost'
$env:POSTGRES_PORT = '5432'
$env:POSTGRES_DB = 'ETL_pipeline_project'
$env:POSTGRES_USER = 'postgres'
$env:POSTGRES_PASSWORD = 'postgres'
```

### macOS / Linux (bash or zsh)

```bash
export POSTGRES_HOST='localhost'
export POSTGRES_PORT='5432'
export POSTGRES_DB='ETL_pipeline_project'
export POSTGRES_USER='postgres'
export POSTGRES_PASSWORD='postgres'
```

## Running the Pipeline

Run the ETL pipeline with the appropriate Python command for your project.

```bash
python ETL.py
```

Replace `ETL.py` with the main script filename if it differs.

## Notes

- Ensure PostgreSQL is running and accessible on the configured host and port.
- Update the environment variables if your database settings differ.
