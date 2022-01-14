# Wind Processing

*By Shiqi Xu, under guidance of Felix Vogel and Sebastien Ars (ECCC), during summer 2021.*


## Overview

Wind data was collected on devices mounted to the mobile platform. Correction is necessary for older devices as they are unable to automatically collect the required information or accurately self-correct for the motion of the platform.

See Jupyter notebooks for more detailed documentation.

The goal for files 1 through 3b below was to correct winds from 2018 that were measured on the old device before the Airmar was employed.

Plumes modelled in Polyphemus are stored on the VM and not documented here.


## Files

### 1. `src/wind_processing/wind_correction_sync_data.ipynb`

The first attempt at correction of wind data. This was mostly good. Corrected winds looked decent. However, there were a few issues, including inconsistent wind directions and complete lack on data on one day (the latter was later solved).

----------------------------------------

### 2. `src/wind_processing/wind_correction_raw_data.ipynb`

Due to issues described above, we decided to retrieve the raw data and work from there to identify the issues. Here I had unnecessarily processed GPS data collected by both Sebastien's watch and Felix's phone (the two overlap for the most part, with Sebastien's having more frequent data points).

----------------------------------------

### 3. a. `src/wind_processing/generate_sync_data_from_raw.ipynb`

Decided to break down the processing of the raw data into 2 Jupyter notebooks. This one specifically handles generating one set of "sync" data that combines that of the GPS, the meteo station, and the Picarro. Here wind correction is also taken care of, by first calculating the car speed & direction.

----------------------------------------

### 3. b. `src/wind_processing/wind_processing_sync_data_from_raw.ipynb`

Here averaging of the winds is done to smooth out fluctuations, as well as plotting. Figures were saved to subdirectories under `fig`.

----------------------------------------

### X. `src/pressure_profiles/pressure_profiles.ipynb`

Investigated the possibility that measured fluxes were influenced by pressure gradients. Context was Polyphemus modelling for German Mills Settlers Park, in which 2 drastically different flux ranges were obtained.

----------------------------------------
