# WCRP Universe - Contribution Guidelines

Welcome to the WCRP Universe repository! This repository contains the universal controlled vocabularies (CVs) shared across WCRP climate modeling projects including CMIP7.

## How to Contribute

Use the issue templates below to add or modify controlled vocabulary entries. All submissions go through a review process before being merged into the official vocabularies.

### Before You Submit

1. **Check existing entries**: Search the repository to ensure your entry doesn't already exist
2. **Use correct formatting**: Follow the naming conventions (lowercase, hyphenated identifiers)
3. **Provide descriptions**: Clear descriptions help users understand each term

### Data Format

All entries use JSON-LD format with standard fields:
- `validation_key`: Unique identifier (lowercase, hyphenated)
- `ui_label`: Human-readable display name  
- `description`: Detailed description of the term
- `alias`: Alternative names (optional)



## 1. Submitting New Controlled Vocabularies

The following forms are available for this repository, and can be used to add or modify entries. The complete submission pipeline (if applicable) will be outlined in the section above.

### Core CVs

- [frequency](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=frequency.yml)
- [realm](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=realm.yml)
- [resolution](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=resolution.yml)
- [source_type](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=source_type.yml)
### Model Structure

- [model_calendar](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=model_calendar.yml)
- [model_component_type](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=model_component_type.yml)
- [model_family](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=model_family.yml)
- [scientific_domain](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=scientific_domain.yml)
### Grid Specifications

- [arrangement](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=arrangement.yml)
- [calendar](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=calendar.yml)
- [grid_mapping](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=grid_mapping.yml)
- [grid_type](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=grid_type.yml)
- [native_horizontal_grid_region](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=native_horizontal_grid_region.yml)
- [native_horizontal_grid_temporal_refinement](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=native_horizontal_grid_temporal_refinement.yml)
- [native_horizontal_grid_type](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=native_horizontal_grid_type.yml)
- [native_vertical_grid_coordinate](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=native_vertical_grid_coordinate.yml)
- [native_vertical_grid_units](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=native_vertical_grid_units.yml)
- [region](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=region.yml)
- [temporal_refinement](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=temporal_refinement.yml)
- [truncation_method](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=truncation_method.yml)
- [units](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=units.yml)
- [vertical_coordinate](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=vertical_coordinate.yml)
### Other

- [cell_variable_type](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=cell_variable_type.yml)

## 2. Modifying or reusing existing entries

The following links will open pre-filled GitHub issues with content from the selected files. These can be used to update entries or make new ones. 

<details markdown="1" name="arrangement">
<summary>Arrangement (5 entries)</summary>

- [arakawa-a](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=arrangement.yml&title=Modify%3A+Arrangement%3A+arakawa-a&issue_kind=%22Modify%22&description=The+Arakawa+A+grid+places+mass-+and+velocity-related+quantities+at+the+same+location+on+each+grid+cell.&ui_label=Arakawa+A-grid&validation_key=arakawa-a)

- [arakawa-b](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=arrangement.yml&title=Modify%3A+Arrangement%3A+arakawa-b&issue_kind=%22Modify%22&description=The+Arakawa+B+grid+places+velocity-related+quantities+at+the+corners+of+mass+cells.&ui_label=Arakawa+B-grid&validation_key=arakawa-b)

- [arakawa-c](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=arrangement.yml&title=Modify%3A+Arrangement%3A+arakawa-c&issue_kind=%22Modify%22&description=The+Arakawa+C+grid+places+velocity-related+quantities+at+the+centres+of+mass+cell+edges%2C+such+that+each+component+is+perpendicular+to+its+edge.&ui_label=Arakawa+C-grid&validation_key=arakawa-c)

- [arakawa-d](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=arrangement.yml&title=Modify%3A+Arrangement%3A+arakawa-d&issue_kind=%22Modify%22&description=The+Arakawa+D+grid+places+velocity-related+quantities+at+the+centres+of+mass+cell+edges%2C+such+that+each+component+is+tangential+to+its+edge.&ui_label=Arakawa+D-grid&validation_key=arakawa-d)

- [arakawa-e](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=arrangement.yml&title=Modify%3A+Arrangement%3A+arakawa-e&issue_kind=%22Modify%22&description=The+Arakawa+E+grid+places+mass-related+quantities+at+the+centres+of+velocity+cell+edges.&ui_label=Arakawa+E-grid&validation_key=arakawa-e)

</details>

<details markdown="1" name="calendar">
<summary>Calendar (9 entries)</summary>

- [360-day](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=calendar.yml&title=Modify%3A+Calendar%3A+360-day&issue_kind=%22Modify%22&description=A+calendar+in+which+each+year+consists+of+12+months+of+exactly+30+days+each.+This+calendar+is+commonly+used+in+climate+models+for+computational+convenience.&ui_label=360-day&alias=&validation_key=360-day)

- [365-day](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=calendar.yml&title=Modify%3A+Calendar%3A+365-day&issue_kind=%22Modify%22&description=A+calendar+in+which+each+year+consists+of+365+days+with+no+leap+years.+All+months+have+their+standard+lengths+%2828+days+for+February%29.&ui_label=365-day+%28No+Leap%29&alias=noleap&validation_key=365-day)

- [366-day](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=calendar.yml&title=Modify%3A+Calendar%3A+366-day&issue_kind=%22Modify%22&description=A+calendar+in+which+each+year+consists+of+366+days%2C+i.e.%2C+every+year+is+a+leap+year+with+February+having+29+days.&ui_label=366-day+%28All+Leap%29&alias=all-leap&validation_key=366-day)

- [julian](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=calendar.yml&title=Modify%3A+Calendar%3A+julian&issue_kind=%22Modify%22&description=Julian+calendar+with+leap+year+every+four+years+without+exception.+This+calendar+was+in+use+prior+to+the+Gregorian+calendar+reform+of+1582.&ui_label=Julian&alias=&validation_key=julian)

- [none](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=calendar.yml&title=Modify%3A+Calendar%3A+none&issue_kind=%22Modify%22&description=No+calendar+-+used+for+data+without+a+temporal+dimension+or+for+time-invariant+fields.&ui_label=None&alias=&validation_key=none)

- [proleptic-gregorian](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=calendar.yml&title=Modify%3A+Calendar%3A+proleptic-gregorian&issue_kind=%22Modify%22&description=A+calendar+with+the+Gregorian+rules+for+leap-years+extended+to+dates+before+1582-10-15.+All+dates+consistent+with+these+rules+are+allowed%2C+both+before+and+after+1582-10-15.&ui_label=Proleptic+Gregorian&alias=&validation_key=proleptic-gregorian)

- [standard](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=calendar.yml&title=Modify%3A+Calendar%3A+standard&issue_kind=%22Modify%22&description=Mixed+Gregorian%2FJulian+calendar+as+defined+by+UDUNITS.+This+is+the+default+calendar+assumed+if+no+calendar+attribute+is+specified.+A+deprecated+alternative+name+for+this+calendar+is+%27gregorian%27.&ui_label=Standard+%28Gregorian%29&alias=gregorian&validation_key=standard)

- [tai](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=calendar.yml&title=Modify%3A+Calendar%3A+tai&issue_kind=%22Modify%22&description=The+Gregorian+calendar+without+leap+seconds+that+is+based+on+International+Atomic+Time+%28TAI%29%2C+as+defined+by+the+CF+conventions.&ui_label=TAI&alias=&validation_key=tai)

- [utc](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=calendar.yml&title=Modify%3A+Calendar%3A+utc&issue_kind=%22Modify%22&description=The+Gregorian+calendar+with+leap+seconds+prescribed+by+Coordinated+Universal+Time+%28UTC%29%2C+as+defined+by+the+CF+conventions.&ui_label=UTC&alias=&validation_key=utc)

</details>

<details markdown="1" name="cell_variable_type">
<summary>Cell Variable Type (5 entries)</summary>

- [mass](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=cell_variable_type.yml&title=Modify%3A+Cell+Variable+Type%3A+mass&issue_kind=%22Modify%22&description=Mass-related+variables%2C+including+those+representing+thermodynamic+and+hydrodynamic+quantities.&ui_label=Mass&validation_key=mass)

- [velocity](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=cell_variable_type.yml&title=Modify%3A+Cell+Variable+Type%3A+velocity&issue_kind=%22Modify%22&description=Variables+representing+the+velocity+vector+when+it+is+not+partitioned+into+X+and+Y+components+%28such+as+for+some+unstructured+grids%29.&ui_label=Velocity&validation_key=velocity)

- [vorticity](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=cell_variable_type.yml&title=Modify%3A+Cell+Variable+Type%3A+vorticity&issue_kind=%22Modify%22&description=Vorticity+and+related+rotational+variables.&ui_label=Vorticity&validation_key=vorticity)

- [x-velocity](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=cell_variable_type.yml&title=Modify%3A+Cell+Variable+Type%3A+x-velocity&issue_kind=%22Modify%22&description=Variables+representing+the+X+component+of+the+velocity+vector+and+certain+horizontal+fluxes+of+mass%2C+energy%2C+momentum%2C+etc.+For+a+grid+defined+by+spherical+polar+coordinates%2C+the+X+direction+is+longitude.&ui_label=X+Velocity&validation_key=x-velocity)

- [y-velocity](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=cell_variable_type.yml&title=Modify%3A+Cell+Variable+Type%3A+y-velocity&issue_kind=%22Modify%22&description=Variables+representing+the+Y+component+of+the+velocity+vector+and+certain+horizontal+fluxes+of+mass%2C+energy%2C+momentum%2C+etc.+For+a+grid+defined+by+spherical+polar+coordinates%2C+the+Y+direction+is+latitude.&ui_label=Y+Velocity&validation_key=y-velocity)

</details>

<details markdown="1" name="frequency">
<summary>Frequency (16 entries)</summary>

- [1hrCM](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=frequency.yml&title=Modify%3A+Frequency%3A+1hrCM&issue_kind=%22Modify%22&description=monthly-mean+diurnal+cycle+resolving+each+day+into+1-hour+means&ui_label=1+Hour+Climatology+Monthly&validation_key=1hrCM)

- [1hrPt](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=frequency.yml&title=Modify%3A+Frequency%3A+1hrPt&issue_kind=%22Modify%22&description=sampled+hourly%2C+at+specified+time+point+within+an+hour&ui_label=1+Hour+Point&validation_key=1hrPt)

- [1hr](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=frequency.yml&title=Modify%3A+Frequency%3A+1hr&issue_kind=%22Modify%22&description=sampled+hourly&ui_label=1+Hourly+Frequency&validation_key=1hr)

- [3hrPt](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=frequency.yml&title=Modify%3A+Frequency%3A+3hrPt&issue_kind=%22Modify%22&description=sampled+3+hourly%2C+at+specified+time+point+within+the+time+period&ui_label=3+Hour+Point&validation_key=3hrPt)

- [3hr](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=frequency.yml&title=Modify%3A+Frequency%3A+3hr&issue_kind=%22Modify%22&description=3+hourly+mean+samples&ui_label=3+Hourly+Frequency&validation_key=3hr)

- [6hrPt](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=frequency.yml&title=Modify%3A+Frequency%3A+6hrPt&issue_kind=%22Modify%22&description=sampled+6+hourly%2C+at+specified+time+point+within+the+time+period&ui_label=6+Hour+Point&validation_key=6hrPt)

- [6hr](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=frequency.yml&title=Modify%3A+Frequency%3A+6hr&issue_kind=%22Modify%22&description=6+hourly+mean+samples&ui_label=6+Hourly+Frequency&validation_key=6hr)

- [day](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=frequency.yml&title=Modify%3A+Frequency%3A+day&issue_kind=%22Modify%22&description=daily+mean+samples&ui_label=Daily+Frequency&validation_key=day)

- [dec](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=frequency.yml&title=Modify%3A+Frequency%3A+dec&issue_kind=%22Modify%22&description=decadal+mean+samples&ui_label=Decadal+Frequency&validation_key=dec)

- [fx](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=frequency.yml&title=Modify%3A+Frequency%3A+fx&issue_kind=%22Modify%22&description=fixed+%28time+invariant%29+field&ui_label=Fixed+Frequency&validation_key=fx)

- [monC](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=frequency.yml&title=Modify%3A+Frequency%3A+monC&issue_kind=%22Modify%22&description=monthly+climatology+computed+from+monthly+mean+samples&ui_label=Monthly+Climatology&validation_key=monC)

- [monPt](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=frequency.yml&title=Modify%3A+Frequency%3A+monPt&issue_kind=%22Modify%22&description=sampled+monthly%2C+at+specified+time+point+within+the+time+period&ui_label=Monthly+Point&validation_key=monPt)

- [mon](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=frequency.yml&title=Modify%3A+Frequency%3A+mon&issue_kind=%22Modify%22&description=monthly+mean+samples&ui_label=Monthly+Frequency&validation_key=mon)

- [subhrPt](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=frequency.yml&title=Modify%3A+Frequency%3A+subhrPt&issue_kind=%22Modify%22&description=sampled+sub-hourly%2C+at+specified+time+point+within+an+hour&ui_label=Sub-Hourly+Point&validation_key=subhrPt)

- [yrPt](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=frequency.yml&title=Modify%3A+Frequency%3A+yrPt&issue_kind=%22Modify%22&description=sampled+yearly%2C+at+specified+time+point+within+the+time+period&ui_label=Yearly+Point&validation_key=yrPt)

- [yr](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=frequency.yml&title=Modify%3A+Frequency%3A+yr&issue_kind=%22Modify%22&description=annual+mean+samples&ui_label=Yearly+Frequency&validation_key=yr)

</details>

<details markdown="1" name="grid_mapping">
<summary>Grid Mapping (16 entries)</summary>

- [albers-conical-equal-area](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=grid_mapping.yml&title=Modify%3A+Grid+Mapping%3A+albers-conical-equal-area&issue_kind=%22Modify%22&description=A+projection+that+preserves+area+but+not+shape%2C+creating+accurate+representations+of+large%2C+east-west-oriented+land+masses%2C+as+defined+by+the+CF+conventions.&ui_label=Albers+Conical+Equal+Area&validation_key=albers-conical-equal-area)

- [azimuthal-equidistant](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=grid_mapping.yml&title=Modify%3A+Grid+Mapping%3A+azimuthal-equidistant&issue_kind=%22Modify%22&description=A+projection+that+maintains+the+correct+distance+and+direction+from+a+central+point+to+all+other+points+on+the+map%2C+as+defined+by+the+CF+conventions.&ui_label=Azimuthal+Equidistant&validation_key=azimuthal-equidistant)

- [geostationary](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=grid_mapping.yml&title=Modify%3A+Grid+Mapping%3A+geostationary&issue_kind=%22Modify%22&description=A+type+of+azimuthal+projection+designed+to+show+the+Earth+as+it+appears+to+a+geostationary+satellite%2C+offering+a+perspective+that+minimizes+distortion+for+areas+under+view%2C+as+defined+by+the+CF+conventions.&ui_label=Geostationary&validation_key=geostationary)

- [healpix](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=grid_mapping.yml&title=Modify%3A+Grid+Mapping%3A+healpix&issue_kind=%22Modify%22&description=The+hierarchical+equal+area+isolatitude+pixelisation+of+a+sphere+based+on+subdivision+of+a+distorted+rhombic+dodecahedron+%28HEALPix%29%2C+as+defined+by+the+CF+conventions.&ui_label=HEALPix&validation_key=healpix)

- [lambert-azimuthal-equal-area](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=grid_mapping.yml&title=Modify%3A+Grid+Mapping%3A+lambert-azimuthal-equal-area&issue_kind=%22Modify%22&description=A+projection+that+accurately+preserves+the+area+of+all+regions+on+a+map%2C+as+defined+by+the+CF+conventions.&ui_label=Lambert+Azimuthal+Equal+Area&validation_key=lambert-azimuthal-equal-area)

- [lambert-conformal-conic](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=grid_mapping.yml&title=Modify%3A+Grid+Mapping%3A+lambert-conformal-conic&issue_kind=%22Modify%22&description=A+projection+that+preserves+the+shape+of+small+areas+by+using+a+cone+placed+over+the+Earth%27s+surface%2C+with+the+projection+onto+the+cone+occurring+along+lines+radiating+from+the+Earth%27s+centre%2C+as+defined+by+the+CF+conventions.&ui_label=Lambert+Conformal+Conic&validation_key=lambert-conformal-conic)

- [lambert-cylindrical-equal-area](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=grid_mapping.yml&title=Modify%3A+Grid+Mapping%3A+lambert-cylindrical-equal-area&issue_kind=%22Modify%22&description=A+cylindrical+map+projection+that+preserves+area+accurately+but+distorts+shape%2C+especially+away+from+the+equator%2C+as+defined+by+the+CF+conventions.&ui_label=Lambert+Cylindrical+Equal+Area&validation_key=lambert-cylindrical-equal-area)

- [latitude-longitude](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=grid_mapping.yml&title=Modify%3A+Grid+Mapping%3A+latitude-longitude&issue_kind=%22Modify%22&description=A+projection+that+treats+latitude+and+longitude+as+planar+X+and+Y+coordinates%2C+as+defined+by+the+CF+conventions.&ui_label=Latitude-Longitude&validation_key=latitude-longitude)

- [mercator](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=grid_mapping.yml&title=Modify%3A+Grid+Mapping%3A+mercator&issue_kind=%22Modify%22&description=Cylindrical+map+projection+preserving+angles%2C+commonly+used+for+ocean+models.&ui_label=Mercator&validation_key=mercator)

- [orthographic](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=grid_mapping.yml&title=Modify%3A+Grid+Mapping%3A+orthographic&issue_kind=%22Modify%22&description=A+form+of+parallel+projection+in+which+all+the+projection+lines+are+orthogonal+to+the+projection+plane%2C+as+defined+by+the+CF+conventions.&ui_label=Orthographic&validation_key=orthographic)

- [polar-stereographic](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=grid_mapping.yml&title=Modify%3A+Grid+Mapping%3A+polar-stereographic&issue_kind=%22Modify%22&description=An+azimuthal+projection+that+maps+the+Earth%27s+surface+onto+a+flat+plane+from+a+view+point+at+one+pole%2C+projecting+points+from+the+globe+to+a+plane+tangent+to+the+opposite+pole%2C+as+defined+by+the+CF+conventions.&ui_label=Polar+Stereographic&validation_key=polar-stereographic)

- [rotated-latitude-longitude](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=grid_mapping.yml&title=Modify%3A+Grid+Mapping%3A+rotated-latitude-longitude&issue_kind=%22Modify%22&description=A+geographic+coordinate+system+where+the+traditional+north+pole+is+shifted+to+a+different+location%2C+as+defined+by+the+CF+conventions.&ui_label=Rotated+Latitude-Longitude&validation_key=rotated-latitude-longitude)

- [sinusoidal](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=grid_mapping.yml&title=Modify%3A+Grid+Mapping%3A+sinusoidal&issue_kind=%22Modify%22&description=An+equal-area+projection+that+accurately+represents+area+but+distorts+shape%2C+especially+at+the+edges%2C+as+defined+by+the+CF+conventions.&ui_label=Sinusoidal&validation_key=sinusoidal)

- [stereographic](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=grid_mapping.yml&title=Modify%3A+Grid+Mapping%3A+stereographic&issue_kind=%22Modify%22&description=A+projection+that+preserves+the+angles+between+intersecting+lines+and+curves+on+the+sphere%2C+as+defined+by+the+CF+conventions.&ui_label=Stereographic&validation_key=stereographic)

- [transverse-mercator](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=grid_mapping.yml&title=Modify%3A+Grid+Mapping%3A+transverse-mercator&issue_kind=%22Modify%22&description=A+projection+that+rotates+the+Mercator+projection+cylinder+90+degrees+to+be+tangent+to+the+Earth+along+a+meridian+instead+of+the+equator%2C+as+defined+by+the+CF+conventions.&ui_label=Transverse+Mercator&validation_key=transverse-mercator)

- [vertical-perspective](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=grid_mapping.yml&title=Modify%3A+Grid+Mapping%3A+vertical-perspective&issue_kind=%22Modify%22&description=A+projection+used+to+represent+the+Earth+from+a+point+of+view+directly+above+its+centre%2C+as+defined+by+the+CF+conventions.&ui_label=Vertical+Perspective&validation_key=vertical-perspective)

</details>

<details markdown="1" name="grid_type">
<summary>Grid Type (23 entries)</summary>

- [cubed-sphere](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=grid_type.yml&title=Modify%3A+Grid+Type%3A+cubed-sphere&issue_kind=%22Modify%22&description=The+spherical+surface+is+defined+as+six+coupled+logically+square+regions.&ui_label=Cubed+Sphere&validation_key=cubed-sphere)

- [cubic-octahedral-spectral-reduced-gaussian](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=grid_type.yml&title=Modify%3A+Grid+Type%3A+cubic-octahedral-spectral-reduced-gaussian&issue_kind=%22Modify%22&description=A+spectral+reduced+Gaussian+grid+for+which+the+smallest+spectral+wavelength+is+represented+by+4+grid+points%2C+and+which+uses+an+octahedron-based+method+to+reduce+the+number+of+grid+points+towards+the+poles.&ui_label=Cubic+Octahedral+Spectral+Reduced+Gaussian&validation_key=cubic-octahedral-spectral-reduced-gaussian)

- [displaced-pole](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=grid_type.yml&title=Modify%3A+Grid+Type%3A+displaced-pole&issue_kind=%22Modify%22&description=An+ocean+grid+whose+poles+are+not+antipodean%2C+typically+with+the+northern+pole+displaced+to+lie+over+land.&ui_label=Displaced+Pole&validation_key=displaced-pole)

- [hierarchical-discrete-global-grid](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=grid_type.yml&title=Modify%3A+Grid+Type%3A+hierarchical-discrete-global-grid&issue_kind=%22Modify%22&description=A+tessellation+of+cells+that+exhaustively+cover+the+spherical+surface+of+the+globe%2C+with+each+resolution+defined+as+a+subdivision+of+cells+at+a+base+resolution%2C+and+cells+at+a+given+resolution+having+equal+areas.&ui_label=Hierarchical+Discrete+Global+Grid&validation_key=hierarchical-discrete-global-grid)

- [icosahedral-geodesic-dual](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=grid_type.yml&title=Modify%3A+Grid+Type%3A+icosahedral-geodesic-dual&issue_kind=%22Modify%22&description=A+grid+that+uses+hexagonal+and+pentagonal+tiles+and+is+the+dual+of+an+icosahedral_geodesic+grid.&ui_label=Icosahedral+Geodesic+Dual&validation_key=icosahedral-geodesic-dual)

- [icosahedral-geodesic](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=grid_type.yml&title=Modify%3A+Grid+Type%3A+icosahedral-geodesic&issue_kind=%22Modify%22&description=A+grid+that+uses+triangular+tiles+based+on+the+subdivision+of+an+icosahedron.&ui_label=Icosahedral+Geodesic&validation_key=icosahedral-geodesic)

- [icosahedral](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=grid_type.yml&title=Modify%3A+Grid+Type%3A+icosahedral&issue_kind=%22Modify%22&description=Grid+based+on+subdividing+an+icosahedron+projected+onto+a+sphere%2C+providing+quasi-uniform+global+coverage.&ui_label=Icosahedral&validation_key=icosahedral)

- [linear-spectral-gaussian](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=grid_type.yml&title=Modify%3A+Grid+Type%3A+linear-spectral-gaussian&issue_kind=%22Modify%22&description=A+spectral+Gaussian+grid+for+which+the+smallest+spectral+wavelength+is+represented+by+2+grid+points.&ui_label=Linear+Spectral+Gaussian&validation_key=linear-spectral-gaussian)

- [plane-projection](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=grid_type.yml&title=Modify%3A+Grid+Type%3A+plane-projection&issue_kind=%22Modify%22&description=Any+transformation+employed+to+represent+the+spherical+surface+of+the+globe+on+a+plane.&ui_label=Plane+Projection&validation_key=plane-projection)

- [quadratic-spectral-gaussian](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=grid_type.yml&title=Modify%3A+Grid+Type%3A+quadratic-spectral-gaussian&issue_kind=%22Modify%22&description=A+spectral+Gaussian+grid+for+which+the+smallest+spectral+wavelength+is+represented+by+3+grid+points.&ui_label=Quadratic+Spectral+Gaussian&validation_key=quadratic-spectral-gaussian)

- [reduced-gaussian](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=grid_type.yml&title=Modify%3A+Grid+Type%3A+reduced-gaussian&issue_kind=%22Modify%22&description=A+Gaussian+grid+for+which+the+number+of+longitudinal+points+is+reduced+as+the+poles+are+approached.&ui_label=Reduced+Gaussian&validation_key=reduced-gaussian)

- [regular-gaussian](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=grid_type.yml&title=Modify%3A+Grid+Type%3A+regular-gaussian&issue_kind=%22Modify%22&description=A+Gaussian+grid+for+which+the+number+of+longitudinal+points+is+constant+for+each+latitude.&ui_label=Regular+Gaussian&validation_key=regular-gaussian)

- [regular-latitude-longitude](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=grid_type.yml&title=Modify%3A+Grid+Type%3A+regular-latitude-longitude&issue_kind=%22Modify%22&description=A+rectilinear+latitude-longitude+grid+with+evenly+spaced+latitude+points+and+evenly+spaced+longitude+points.&ui_label=Regular+Latitude-Longitude&validation_key=regular-latitude-longitude)

- [rotated-pole](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=grid_type.yml&title=Modify%3A+Grid+Type%3A+rotated-pole&issue_kind=%22Modify%22&description=A+regular+latitude-longitude+grid+that+is+rotated+to+define+a+different+north+pole+location.&ui_label=Rotated+Pole&validation_key=rotated-pole)

- [spectral-gaussian](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=grid_type.yml&title=Modify%3A+Grid+Type%3A+spectral-gaussian&issue_kind=%22Modify%22&description=A+grid+based+on+the+transformation+from+spectral+space+to+a+reduced+or+non-reduced+Gaussian+grid.&ui_label=Spectral+Gaussian&validation_key=spectral-gaussian)

- [spectral-reduced-gaussian](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=grid_type.yml&title=Modify%3A+Grid+Type%3A+spectral-reduced-gaussian&issue_kind=%22Modify%22&description=A+grid+based+on+the+transformation+from+spectral+space+to+a+reduced+Gaussian+grid.&ui_label=Spectral+Reduced+Gaussian&validation_key=spectral-reduced-gaussian)

- [stretched](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=grid_type.yml&title=Modify%3A+Grid+Type%3A+stretched&issue_kind=%22Modify%22&description=A+grid+with+higher+resolution+concentrated+over+an+area+of+interest%2C+at+the+expense+of+lower+resolution+elsewhere.&ui_label=Stretched&validation_key=stretched)

- [tripolar](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=grid_type.yml&title=Modify%3A+Grid+Type%3A+tripolar&issue_kind=%22Modify%22&description=A+global+curvilinear+ocean+grid+with+a+southern+pole+and+two+northern+poles+all+placed+over+land.&ui_label=Tripolar&validation_key=tripolar)

- [unstructured-polygonal](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=grid_type.yml&title=Modify%3A+Grid+Type%3A+unstructured-polygonal&issue_kind=%22Modify%22&description=An+unstructured+mesh+consisting+of+arbitrary+polygons.&ui_label=Unstructured+Polygonal&validation_key=unstructured-polygonal)

- [unstructured-quadrilateral](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=grid_type.yml&title=Modify%3A+Grid+Type%3A+unstructured-quadrilateral&issue_kind=%22Modify%22&description=An+unstructured+mesh+consisting+solely+of+quadrilaterals.&ui_label=Unstructured+Quadrilateral&validation_key=unstructured-quadrilateral)

- [unstructured-triangular](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=grid_type.yml&title=Modify%3A+Grid+Type%3A+unstructured-triangular&issue_kind=%22Modify%22&description=An+unstructured+mesh+consisting+solely+of+triangles.&ui_label=Unstructured+Triangular&validation_key=unstructured-triangular)

- [unstructured](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=grid_type.yml&title=Modify%3A+Grid+Type%3A+unstructured&issue_kind=%22Modify%22&description=Irregular+mesh+without+fixed+connectivity+pattern%2C+allowing+variable+resolution+and+complex+domain+boundaries.&ui_label=Unstructured&validation_key=unstructured)

- [yin-yang](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=grid_type.yml&title=Modify%3A+Grid+Type%3A+yin-yang&issue_kind=%22Modify%22&description=Two+overlapping+grid+patches.&ui_label=Yin-Yang&validation_key=yin-yang)

</details>

<details markdown="1" name="region">
<summary>Region (9 entries)</summary>

- [30s-90s](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=region.yml&title=Modify%3A+Region%3A+30s-90s&issue_kind=%22Modify%22&description=The+geographical+region+of+the+Earth%27s+surface+between+30+and+90+degrees+south.&ui_label=30S-90S&validation_key=30s-90s)

- [antarctica](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=region.yml&title=Modify%3A+Region%3A+antarctica&issue_kind=%22Modify%22&description=Located+around+the+South+Pole%2C+separated+from+other+land+masses+by+the+Southern+Ocean%2C+and+almost+entirely+south+of+60+degrees+South+latitude.&ui_label=Antarctica&validation_key=antarctica)

- [arctic](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=region.yml&title=Modify%3A+Region%3A+arctic&issue_kind=%22Modify%22&description=The+polar+region+surrounding+the+North+Pole%2C+typically+defined+as+north+of+the+Arctic+Circle+%2866.5%C2%B0N%29+or+north+of+60%C2%B0N+latitude.&ui_label=Arctic&validation_key=arctic)

- [global](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=region.yml&title=Modify%3A+Region%3A+global&issue_kind=%22Modify%22&description=The+complete+Earth+surface%2C+90+degrees+North+to+90+degrees+South+latitude%2C+and+all+longitudes.&ui_label=Global&validation_key=global)

- [greenland](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=region.yml&title=Modify%3A+Region%3A+greenland&issue_kind=%22Modify%22&description=Located+in+the+Northern+Atlantic+Ocean%2C+separated+from+other+land+masses+by+the+Labrador+Sea+and+Straits%2C+and+almost+entirely+north+of+60+degrees+North+latitude.&ui_label=Greenland&validation_key=greenland)

- [limited-area](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=region.yml&title=Modify%3A+Region%3A+limited-area&issue_kind=%22Modify%22&description=Any+contiguous+subregion+of+the+Earth%27s+surface%2C+used+to+indicate+a+limited+area+model+that+may+be+placed+over+different+geographical+regions+independently+of+the+model+formulation.&ui_label=Limited+Area&validation_key=limited-area)

- [northern-hemisphere](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=region.yml&title=Modify%3A+Region%3A+northern-hemisphere&issue_kind=%22Modify%22&description=The+complete+Earth+surface+from+the+equator+to+the+North+Pole%2C+0+to+90+degrees+North+latitude.&ui_label=Northern+Hemisphere&validation_key=northern-hemisphere)

- [southern-hemisphere](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=region.yml&title=Modify%3A+Region%3A+southern-hemisphere&issue_kind=%22Modify%22&description=The+complete+Earth+surface+from+the+equator+to+the+South+Pole%2C+0+to+90+degrees+South+latitude.&ui_label=Southern+Hemisphere&validation_key=southern-hemisphere)

- [tropics](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=region.yml&title=Modify%3A+Region%3A+tropics&issue_kind=%22Modify%22&description=The+tropical+region+between+23.5+degrees+North+and+23.5+degrees+South+latitude%2C+bounded+by+the+Tropic+of+Cancer+and+Tropic+of+Capricorn.&ui_label=Tropics&validation_key=tropics)

</details>

<details markdown="1" name="resolution">
<summary>Resolution (15 entries)</summary>

- [0-5-km](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=resolution.yml&title=Modify%3A+Resolution%3A+0-5-km&issue_kind=%22Modify%22&description=Resolution+of+0.5+km&ui_label=0.5+km&validation_key=0-5-km)

- [1-km](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=resolution.yml&title=Modify%3A+Resolution%3A+1-km&issue_kind=%22Modify%22&description=Resolution+of+1+km&ui_label=1+km&validation_key=1-km)

- [10-km](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=resolution.yml&title=Modify%3A+Resolution%3A+10-km&issue_kind=%22Modify%22&description=Resolution+of+10+km&ui_label=10+km&validation_key=10-km)

- [100-km](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=resolution.yml&title=Modify%3A+Resolution%3A+100-km&issue_kind=%22Modify%22&description=Resolution+of+100+km&ui_label=100+km&validation_key=100-km)

- [1000-km](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=resolution.yml&title=Modify%3A+Resolution%3A+1000-km&issue_kind=%22Modify%22&description=Resolution+of+1000+km&ui_label=1000+km&validation_key=1000-km)

- [10000-km](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=resolution.yml&title=Modify%3A+Resolution%3A+10000-km&issue_kind=%22Modify%22&description=Resolution+of+10000+km&ui_label=10000+km&validation_key=10000-km)

- [1x1-degree](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=resolution.yml&title=Modify%3A+Resolution%3A+1x1-degree&issue_kind=%22Modify%22&description=Resolution+of+1x1+degree&ui_label=1x1+Degree&validation_key=1x1-degree)

- [2-5-km](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=resolution.yml&title=Modify%3A+Resolution%3A+2-5-km&issue_kind=%22Modify%22&description=Resolution+of+2.5+km&ui_label=2.5+km&validation_key=2-5-km)

- [25-km](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=resolution.yml&title=Modify%3A+Resolution%3A+25-km&issue_kind=%22Modify%22&description=Resolution+of+25+km&ui_label=25+km&validation_key=25-km)

- [250-km](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=resolution.yml&title=Modify%3A+Resolution%3A+250-km&issue_kind=%22Modify%22&description=Resolution+of+250+km&ui_label=250+km&validation_key=250-km)

- [2500-km](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=resolution.yml&title=Modify%3A+Resolution%3A+2500-km&issue_kind=%22Modify%22&description=Resolution+of+2500+km&ui_label=2500+km&validation_key=2500-km)

- [5-km](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=resolution.yml&title=Modify%3A+Resolution%3A+5-km&issue_kind=%22Modify%22&description=Resolution+of+5+km&ui_label=5+km&validation_key=5-km)

- [50-km](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=resolution.yml&title=Modify%3A+Resolution%3A+50-km&issue_kind=%22Modify%22&description=Resolution+of+50+km&ui_label=50+km&validation_key=50-km)

- [500-km](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=resolution.yml&title=Modify%3A+Resolution%3A+500-km&issue_kind=%22Modify%22&description=Resolution+of+500+km&ui_label=500+km&validation_key=500-km)

- [5000-km](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=resolution.yml&title=Modify%3A+Resolution%3A+5000-km&issue_kind=%22Modify%22&description=Resolution+of+5000+km&ui_label=5000+km&validation_key=5000-km)

</details>

<details markdown="1" name="scientific_domain">
<summary>Scientific Domain (8 entries)</summary>

- [aerosol](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=scientific_domain.yml&title=Modify%3A+Scientific+Domain%3A+aerosol&issue_kind=%22Modify%22&description=Aerosol&ui_label=Aerosol&alias=aerosol&validation_key=aerosol)

- [atmosphere](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=scientific_domain.yml&title=Modify%3A+Scientific+Domain%3A+atmosphere&issue_kind=%22Modify%22&description=Atmosphere&ui_label=Atmosphere&alias=atmos&validation_key=atmosphere)

- [atmospheric-chemistry](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=scientific_domain.yml&title=Modify%3A+Scientific+Domain%3A+atmospheric-chemistry&issue_kind=%22Modify%22&description=Atmospheric+Chemistry&ui_label=Atmospheric+Chemistry&alias=atmoschem%2C+atmosChem&validation_key=atmospheric-chemistry)

- [land-ice](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=scientific_domain.yml&title=Modify%3A+Scientific+Domain%3A+land-ice&issue_kind=%22Modify%22&description=Land+Ice&ui_label=Land+Ice&alias=landice%2C+landIce&validation_key=land-ice)

- [land_surface](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=scientific_domain.yml&title=Modify%3A+Scientific+Domain%3A+land_surface&issue_kind=%22Modify%22&description=Land+Surface+and+Subsurface&ui_label=Land+Surface+and+Subsurface&alias=land&validation_key=land_surface)

- [ocean-biogeochemistry](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=scientific_domain.yml&title=Modify%3A+Scientific+Domain%3A+ocean-biogeochemistry&issue_kind=%22Modify%22&description=Ocean+Biogeochemistry&ui_label=Ocean+Biogeochemistry&alias=ocnbgchem%2C+ocnBgchem&validation_key=ocean-biogeochemistry)

- [ocean](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=scientific_domain.yml&title=Modify%3A+Scientific+Domain%3A+ocean&issue_kind=%22Modify%22&description=Ocean&ui_label=Ocean&alias=ocean&validation_key=ocean)

- [sea_ice](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=scientific_domain.yml&title=Modify%3A+Scientific+Domain%3A+sea_ice&issue_kind=%22Modify%22&description=Sea+Ice&ui_label=Sea+Ice&alias=seaice%2C+seaIce&validation_key=sea_ice)

</details>

<details markdown="1" name="source_type">
<summary>Source Type (14 entries)</summary>

- [AER](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=source_type.yml&title=Modify%3A+Source+Type%3A+AER&issue_kind=%22Modify%22&description=aerosol+treatment+in+an+atmospheric+model+where+concentrations+are+calculated+based+on+emissions%2C+transformation%2C+and+removal+processes+%28rather+than+being+prescribed+or+omitted+entirely%29&ui_label=&validation_key=AER)

- [AGCM](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=source_type.yml&title=Modify%3A+Source+Type%3A+AGCM&issue_kind=%22Modify%22&description=atmospheric+general+circulation+model+run+with+prescribed+ocean+surface+conditions+and+usually+a+model+of+the+land+surface&ui_label=&validation_key=AGCM)

- [AOGCM](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=source_type.yml&title=Modify%3A+Source+Type%3A+AOGCM&issue_kind=%22Modify%22&description=coupled+atmosphere-ocean+global+climate+model%2C+additionally+including+explicit+representation+of+at+least+the+land+and+sea+ice&ui_label=&validation_key=AOGCM)

- [BGC](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=source_type.yml&title=Modify%3A+Source+Type%3A+BGC&issue_kind=%22Modify%22&description=biogeochemistry+model+component+that+at+the+very+least+accounts+for+carbon+reservoirs+and+fluxes+in+the+atmosphere%2C+terrestrial+biosphere%2C+and+ocean&ui_label=&validation_key=BGC)

- [CHEM](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=source_type.yml&title=Modify%3A+Source+Type%3A+CHEM&issue_kind=%22Modify%22&description=chemistry+treatment+in+an+atmospheric+model+that+calculates+atmospheric+oxidant+concentrations+%28including+at+least+ozone%29%2C+rather+than+prescribing+them&ui_label=&validation_key=CHEM)

- [ISM](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=source_type.yml&title=Modify%3A+Source+Type%3A+ISM&issue_kind=%22Modify%22&description=ice-sheet+model+that+includes+ice-flow&ui_label=&validation_key=ISM)

- [LAND](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=source_type.yml&title=Modify%3A+Source+Type%3A+LAND&issue_kind=%22Modify%22&description=land+model+run+uncoupled+from+the+atmosphere&ui_label=&validation_key=LAND)

- [OGCM](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=source_type.yml&title=Modify%3A+Source+Type%3A+OGCM&issue_kind=%22Modify%22&description=ocean+general+circulation+model+run+uncoupled+from+an+AGCM+but%2C+usually+including+a+sea-ice+model&ui_label=&validation_key=OGCM)

- [RAD](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=source_type.yml&title=Modify%3A+Source+Type%3A+RAD&issue_kind=%22Modify%22&description=radiation+component+of+an+atmospheric+model+run+%27offline%27&ui_label=&validation_key=RAD)

- [SLAB](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=source_type.yml&title=Modify%3A+Source+Type%3A+SLAB&issue_kind=%22Modify%22&description=slab-ocean+used+with+an+AGCM+in+representing+the+atmosphere-ocean+coupled+system&ui_label=&validation_key=SLAB)

- [gridded-insitu](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=source_type.yml&title=Modify%3A+Source+Type%3A+gridded-insitu&issue_kind=%22Modify%22&description=gridded+product+based+on+measurements+collected+from+in-situ+instruments&ui_label=&validation_key=gridded-insitu)

- [reanalysis](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=source_type.yml&title=Modify%3A+Source+Type%3A+reanalysis&issue_kind=%22Modify%22&description=gridded+product+generated+from+a+model+reanalysis+based+on+in-situ+instruments+and+possibly+satellite+measurements&ui_label=&validation_key=reanalysis)

- [satellite-blended](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=source_type.yml&title=Modify%3A+Source+Type%3A+satellite-blended&issue_kind=%22Modify%22&description=gridded+product+based+on+both+in-situ+instruments+and+satellite+measurements&ui_label=&validation_key=satellite-blended)

- [satellite-retrieval](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=source_type.yml&title=Modify%3A+Source+Type%3A+satellite-retrieval&issue_kind=%22Modify%22&description=gridded+product+based+on+satellite+measurements&ui_label=&validation_key=satellite-retrieval)

</details>

<details markdown="1" name="temporal_refinement">
<summary>Temporal Refinement (3 entries)</summary>

- [adaptive](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=temporal_refinement.yml&title=Modify%3A+Temporal+Refinement%3A+adaptive&issue_kind=%22Modify%22&description=Grid+resolution+changes+dynamically+during+the+simulation+based+on+solution+features.&ui_label=Adaptive&validation_key=adaptive)

- [dynamically-stretched](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=temporal_refinement.yml&title=Modify%3A+Temporal+Refinement%3A+dynamically-stretched&issue_kind=%22Modify%22&description=The+total+number+of+grid+points+stays+constant%2C+but+grid+points+can+be+dynamically+relocated.&ui_label=Dynamically+Stretched&validation_key=dynamically-stretched)

- [static](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=temporal_refinement.yml&title=Modify%3A+Temporal+Refinement%3A+static&issue_kind=%22Modify%22&description=Grid+resolution+remains+constant+throughout+the+simulation.&ui_label=Static&validation_key=static)

</details>

<details markdown="1" name="truncation_method">
<summary>Truncation Method (2 entries)</summary>

- [rhomboidal](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=truncation_method.yml&title=Modify%3A+Truncation+Method%3A+rhomboidal&issue_kind=%22Modify%22&description=Rhomboidal+truncation+in+spectral+space+where+%7Cm%7C+%E2%89%A4+M+and+%7Cn-m%7C+%E2%89%A4+N.+Provides+more+uniform+resolution+across+latitudes+than+triangular+truncation.&ui_label=Rhomboidal+Truncation&validation_key=rhomboidal)

- [triangular](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=truncation_method.yml&title=Modify%3A+Truncation+Method%3A+triangular&issue_kind=%22Modify%22&description=Triangular+truncation+in+spectral+space+where+total+wavenumber+m%2Bn+%E2%89%A4+N.+Common+notation%3A+TL+%28triangular+linear%29+or+TQ+%28triangular+quadratic%29.&ui_label=Triangular+Truncation&validation_key=triangular)

</details>

<details markdown="1" name="units">
<summary>Units (5 entries)</summary>

- [degree](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=units.yml&title=Modify%3A+Units%3A+degree&issue_kind=%22Modify%22&description=Angular+measurement+in+degrees+for+latitude%2Flongitude+coordinates.&ui_label=Degrees&validation_key=degree)

- [k](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=units.yml&title=Modify%3A+Units%3A+k&issue_kind=%22Modify%22&description=Unit+for+temperature.&ui_label=Kelvin&validation_key=k)

- [km](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=units.yml&title=Modify%3A+Units%3A+km&issue_kind=%22Modify%22&description=Kilometre+%28unit+for+length%29.&ui_label=Kilometre&validation_key=km)

- [meter](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=units.yml&title=Modify%3A+Units%3A+meter&issue_kind=%22Modify%22&description=Distance+measurement+in+meters+for+projected+coordinate+systems.&ui_label=Meters&validation_key=meter)

- [pa](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=units.yml&title=Modify%3A+Units%3A+pa&issue_kind=%22Modify%22&description=Unit+for+pressure.&ui_label=Pascal&validation_key=pa)

</details>

<details markdown="1" name="vertical_coordinate">
<summary>Vertical Coordinate (20 entries)</summary>

- [air-potential-temperature](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=vertical_coordinate.yml&title=Modify%3A+Vertical+Coordinate%3A+air-potential-temperature&issue_kind=%22Modify%22&description=Air+potential+temperature+is+the+temperature+a+parcel+of+air+would+have+if+moved+dry+adiabatically+to+a+standard+pressure%2C+as+defined+by+the+CF+conventions.&ui_label=Air+Potential+Temperature&validation_key=air-potential-temperature)

- [air-pressure](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=vertical_coordinate.yml&title=Modify%3A+Vertical+Coordinate%3A+air-pressure&issue_kind=%22Modify%22&description=Air+pressure+is+the+pressure+that+exists+in+the+medium+of+air%2C+as+defined+by+the+CF+conventions.&ui_label=Air+Pressure&validation_key=air-pressure)

- [atmosphere-hybrid-height-coordinate](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=vertical_coordinate.yml&title=Modify%3A+Vertical+Coordinate%3A+atmosphere-hybrid-height-coordinate&issue_kind=%22Modify%22&description=Parametric+atmosphere+hybrid+height+coordinate%2C+as+defined+by+the+CF+conventions.&ui_label=Atmosphere+Hybrid+Height+Coordinate&validation_key=atmosphere-hybrid-height-coordinate)

- [atmosphere-hybrid-sigma-pressure-coordinate](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=vertical_coordinate.yml&title=Modify%3A+Vertical+Coordinate%3A+atmosphere-hybrid-sigma-pressure-coordinate&issue_kind=%22Modify%22&description=Parametric+atmosphere+hybrid+sigma+pressure+coordinate%2C+as+defined+by+the+CF+conventions.&ui_label=Atmosphere+Hybrid+Sigma+Pressure+Coordinate&validation_key=atmosphere-hybrid-sigma-pressure-coordinate)

- [atmosphere-ln-pressure-coordinate](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=vertical_coordinate.yml&title=Modify%3A+Vertical+Coordinate%3A+atmosphere-ln-pressure-coordinate&issue_kind=%22Modify%22&description=Parametric+atmosphere+natural+log+pressure+coordinate%2C+as+defined+by+the+CF+conventions.&ui_label=Atmosphere+Ln+Pressure+Coordinate&validation_key=atmosphere-ln-pressure-coordinate)

- [atmosphere-sigma-coordinate](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=vertical_coordinate.yml&title=Modify%3A+Vertical+Coordinate%3A+atmosphere-sigma-coordinate&issue_kind=%22Modify%22&description=Parametric+atmosphere+sigma+coordinate%2C+as+defined+by+the+CF+conventions.&ui_label=Atmosphere+Sigma+Coordinate&validation_key=atmosphere-sigma-coordinate)

- [atmosphere-sleve-coordinate](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=vertical_coordinate.yml&title=Modify%3A+Vertical+Coordinate%3A+atmosphere-sleve-coordinate&issue_kind=%22Modify%22&description=Parametric+atmosphere+smooth+vertical+level+coordinate%2C+as+defined+by+the+CF+conventions.&ui_label=Atmosphere+SLEVE+Coordinate&validation_key=atmosphere-sleve-coordinate)

- [depth](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=vertical_coordinate.yml&title=Modify%3A+Vertical+Coordinate%3A+depth&issue_kind=%22Modify%22&description=Vertical+distance+below+a+reference+surface+%28e.g.%2C+sea+surface%2C+land+surface%29.&ui_label=Depth&validation_key=depth)

- [geopotential-height](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=vertical_coordinate.yml&title=Modify%3A+Vertical+Coordinate%3A+geopotential-height&issue_kind=%22Modify%22&description=Geopotential+height+is+the+geopotential+divided+by+the+standard+acceleration+due+to+gravity%2C+as+defined+by+the+CF+conventions.&ui_label=Geopotential+Height&validation_key=geopotential-height)

- [height](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=vertical_coordinate.yml&title=Modify%3A+Vertical+Coordinate%3A+height&issue_kind=%22Modify%22&description=Vertical+distance+above+a+reference+surface.&ui_label=Height&validation_key=height)

- [land-ice-sigma-coordinate](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=vertical_coordinate.yml&title=Modify%3A+Vertical+Coordinate%3A+land-ice-sigma-coordinate&issue_kind=%22Modify%22&description=Land+ice+%28glaciers%2C+ice-caps+and+ice-sheets+resting+on+bedrock+and+also+includes+ice-shelves%29+sigma+coordinate%2C+as+defined+by+the+CF+conventions.&ui_label=Land+Ice+Sigma+Coordinate&validation_key=land-ice-sigma-coordinate)

- [ocean-double-sigma-coordinate](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=vertical_coordinate.yml&title=Modify%3A+Vertical+Coordinate%3A+ocean-double-sigma-coordinate&issue_kind=%22Modify%22&description=Parametric+ocean+double+sigma+coordinate%2C+as+defined+by+the+CF+conventions.&ui_label=Ocean+Double+Sigma+Coordinate&validation_key=ocean-double-sigma-coordinate)

- [ocean-s-coordinate-g1](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=vertical_coordinate.yml&title=Modify%3A+Vertical+Coordinate%3A+ocean-s-coordinate-g1&issue_kind=%22Modify%22&description=Parametric+ocean+s-coordinate%2C+generic+form+1%2C+as+defined+by+the+CF+conventions.&ui_label=Ocean+S+Coordinate+G1&validation_key=ocean-s-coordinate-g1)

- [ocean-s-coordinate-g2](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=vertical_coordinate.yml&title=Modify%3A+Vertical+Coordinate%3A+ocean-s-coordinate-g2&issue_kind=%22Modify%22&description=Parametric+ocean+s-coordinate%2C+generic+form+2%2C+as+defined+by+the+CF+conventions.&ui_label=Ocean+S+Coordinate+G2&validation_key=ocean-s-coordinate-g2)

- [ocean-s-coordinate](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=vertical_coordinate.yml&title=Modify%3A+Vertical+Coordinate%3A+ocean-s-coordinate&issue_kind=%22Modify%22&description=Parametric+ocean+s-coordinate%2C+as+defined+by+the+CF+conventions.&ui_label=Ocean+S+Coordinate&validation_key=ocean-s-coordinate)

- [ocean-sigma-coordinate](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=vertical_coordinate.yml&title=Modify%3A+Vertical+Coordinate%3A+ocean-sigma-coordinate&issue_kind=%22Modify%22&description=Parametric+ocean+sigma+coordinate%2C+as+defined+by+the+CF+conventions.&ui_label=Ocean+Sigma+Coordinate&validation_key=ocean-sigma-coordinate)

- [ocean-sigma-z-coordinate](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=vertical_coordinate.yml&title=Modify%3A+Vertical+Coordinate%3A+ocean-sigma-z-coordinate&issue_kind=%22Modify%22&description=Parametric+ocean+sigma+over+z+coordinate%2C+as+defined+by+the+CF+conventions.&ui_label=Ocean+Sigma+Z+Coordinate&validation_key=ocean-sigma-z-coordinate)

- [sea-water-potential-temperature](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=vertical_coordinate.yml&title=Modify%3A+Vertical+Coordinate%3A+sea-water-potential-temperature&issue_kind=%22Modify%22&description=Sea+water+potential+temperature+is+the+temperature+a+parcel+of+sea+water+would+have+if+moved+adiabatically+to+sea+level+pressure%2C+as+defined+by+the+CF+conventions.&ui_label=Sea+Water+Potential+Temperature&validation_key=sea-water-potential-temperature)

- [sea-water-pressure](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=vertical_coordinate.yml&title=Modify%3A+Vertical+Coordinate%3A+sea-water-pressure&issue_kind=%22Modify%22&description=Sea+water+pressure+is+the+pressure+that+exists+in+the+medium+of+sea+water%2C+as+defined+by+the+CF+conventions.&ui_label=Sea+Water+Pressure&validation_key=sea-water-pressure)

- [z*](https://github.com/WCRP-CMIP/WCRP-constants/issues/new?template=vertical_coordinate.yml&title=Modify%3A+Vertical+Coordinate%3A+z%2A&issue_kind=%22Modify%22&description=The+z%2A+coordinate%2C+as+defined+by+Adcroft+and+Campin+%282004%29.&ui_label=z%2A&validation_key=z%2A)

</details>
