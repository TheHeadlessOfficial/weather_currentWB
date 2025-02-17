import os, sys
from PIL import Image
import time
import requests
# import datetime
# import json
# import pprint
# import textwrap
# from textwrap import dedent
# Lock file to tell conky that the script is running
lock_file = "/tmp/script_wbcurrent.lock"
# Crea il file di lock all'inizio
try:
    open(lock_file, 'w').close()
    ################################ get your HOME automatically
    homepath = os.environ['HOME']
    homename = homepath
    homename = homename[6:]
    ################################ set your latitude, longitude and APPID
    mylat = 45.40713
    mylon = 11.87680
    #    type your APPID between apostrophes
    myAPPID = ''
    ################################ pattern url today
    url = 'https://api.weatherbit.io/v2.0/current?lat=' + str(mylat) + '&lon=' + str(mylon) + '&key=' + myAPPID
    res = requests.get(url).json()
    data = res
    ################################ set variables
    myd = 72 # type your north degree
    tdeg = 0
    winddeg = 0
    vtext = 'n/a'
    ################################ set the paths for the API files
    home = '/home/'
    conky = '/.conkyGITHUB/'
    ptemp = conky + 'weather/Weatherbit/today/'
    ptemp2 = conky + 'weather/compass'
    #                   set the path for the ERROR
    perr = home + homename + ptemp + '-error.txt'
    #                   set the path for the FLAGS
    pflags = home + homename + ptemp + 'flags.txt'
    #                   set the path for today raw data
    ptodayraw = home + homename + ptemp + 'wbtodayraw.txt'
    #                   set the path for today clean data
    ptodayclean = home + homename + ptemp + 'wbtodayclean.txt'
    #                   set the path for the weatherbit logo
    pwblogo = home + homename + ptemp + 'wblogo.txt'
    #                   set the paths for the compass
    parrow = home + homename + ptemp2 + '/arrow.png'
    parrow2 = home + homename + ptemp2 + '/arrow2.png'
    parrowt = home + homename + ptemp2 + '/arrowt.png'
    parrowt2 = home + homename + ptemp2 + '/arrowt2.png'
    pcompass = home + homename + ptemp + 'todaycompass.txt'
    pathwindrose = "${image $HOME" + conky + "weather/compass/windsrose.png -p 305,60 -s 100x100}"
    #                   set the path for today dewpoint
    pdewpoint = home + homename + ptemp + 'todaywbdewpoint.txt'
    #                   set the path for today uv index
    puvindex = home + homename + ptemp + 'todaywbuvindex.txt'
    #                   set the path for today aqi
    paqi = home + homename + ptemp + 'todaywbaqi.txt'
    #                   set the path for the sun duration
    psundur = home + homename + ptemp + 'sunduration.txt'
    #                   set the path for today main icon
    ptodaymainicon = home + homename + ptemp + 'todayicon.txt'
    #                   set the path for today main icon OWM
    ptodaymainiconOWM = home + homename + ptemp + 'todayiconOWM.txt'
    #                   set the path for HOT icon
    photicon = home + homename + ptemp + 'todayiconhotOWM.txt'
    #                   set the path for COLD icon
    pcoldicon = home + homename + ptemp + 'todayiconcoldOWM.txt'
    #                   set the path for the TODAY conky section
    pathtodayconky = home + homename + ptemp + 'todayconky.txt'
    ################################ get data for ERROR section
    try:
        coderr = data['error']
    except:
        coderr = 'ok'
    ################################ write raw data for ERROR section
    fo = open(perr, 'w')
    fo.write('error: {}\n'.format(coderr))
    fo.close()
    ################################ get data for today
    count = data['count']
    tempfeelslike = data['data'][0]['app_temp']
    aqi = data['data'][0]['aqi']
    cityname = data['data'][0]['city_name']
    clouds = data['data'][0]['clouds']
    countrycode = data['data'][0]['country_code']
    datetimec = data['data'][0]['datetime']
    cdewpoint = data['data'][0]['dewpt']
    dhi = data['data'][0]['dhi']
    dni = data['data'][0]['dni']
    elevangle = data['data'][0]['elev_angle']
    ghi = data['data'][0]['ghi']
    try:
        windgust = data['data'][0]['gust']
        # transforms meters/second into Kilometers/hour.
        windgust = round(windgust * 3.6, 2)
    except Exception:
        windspeed = vtext
    hangle = data['data'][0]['h_angle']
    lat = data['data'][0]['lat']
    lon = data['data'][0]['lon']
    obtime = data['data'][0]['ob_time']
    pod = data['data'][0]['pod']
    precip = data['data'][0]['precip']
    pressure = data['data'][0]['pres']
    humidity = data['data'][0]['rh']
    seapressure = data['data'][0]['slp']
    snow = data['data'][0]['snow']
    solarrad = data['data'][0]['solar_rad']
    source0 = data['data'][0]['sources'][0]
    source1 = data['data'][0]['sources'][1]
    source2 = data['data'][0]['sources'][2]
    source3 = data['data'][0]['sources'][3]
    statecode = data['data'][0]['state_code']
    station = data['data'][0]['station']
    sunrise = data['data'][0]['sunrise']
    sunset = data['data'][0]['sunset']
    temp = data['data'][0]['temp']
    timezone = data['data'][0]['timezone']
    timezone = timezone + '        '
    ts = data['data'][0]['ts']
    ts2 = time.strftime("%d-%B-%Y", time.localtime(ts))
    uv = data['data'][0]['uv']
    vis = data['data'][0]['vis']
    desc = data['data'][0]['weather']['description']
    code = data['data'][0]['weather']['code']
    icon = data['data'][0]['weather']['icon']
    winddegabb = data['data'][0]['wind_cdir']
    winddegverb = data['data'][0]['wind_cdir_full']
    winddeg = data['data'][0]['wind_dir']
    windspeed = data['data'][0]['wind_spd']
    #                   disable next row if you set IMPERIAL system in your IDAPP, cause you will get miles/hours. Next row transforms meters/second into Kilometers/hour.
    windspeed = round(windspeed * 3.6, 2)
    ################################ write raw data on a file
    fo = open(ptodayraw, 'w')
    fo.write('Count: {}\n'.format(count))
    fo.write('(feels: {}°C)\n'.format(tempfeelslike))
    fo.write('AQI: {}\n'.format(aqi))
    fo.write('Cityname: {}\n'.format(cityname))
    fo.write('Clouds: {}%\n'.format(clouds))
    fo.write('Countrycode: {}\n'.format(countrycode))
    fo.write('Datetime: {}\n'.format(datetimec))
    fo.write('Dewpoint: {}°C\n'.format(cdewpoint))
    fo.write('Diffuse_horizontal_solar_irradiance_(W/m^2): {} W/m^2\n'.format(dhi))
    fo.write('Direct_normal_solar_irradiance_(W/m^2): {} W/m^2\n'.format(dni))
    fo.write('Elevangle: {}°\n'.format(elevangle))
    fo.write('Global_horizontal_solar_irradiance_(W/m^2): {} W/m^2\n'.format(ghi))
    fo.write('Windgust: {} Km/h\n'.format(windgust))
    fo.write('Hourangle: {}°\n'.format(hangle))
    fo.write('lat: {}\n'.format(lat))
    fo.write('lon: {}\n'.format(lon))
    fo.write('Obtime: {}\n'.format(obtime))
    fo.write('Pod: {}\n'.format(pod))
    fo.write('Rainprecip: {} mm/hr\n'.format(precip))
    fo.write('Pressure: {}m/b\n'.format(pressure))
    fo.write('Humidity: {}%\n'.format(humidity))
    fo.write('SeaPressure: {}m/b\n'.format(seapressure))
    fo.write('Snowprecip: {} mm/hr\n'.format(snow))
    fo.write('Solarrad: {}\n'.format(solarrad))
    fo.write('source0: {}\n'.format(source0))
    fo.write('source1: {}\n'.format(source1))
    fo.write('source2: {}\n'.format(source2))
    fo.write('source3: {}\n'.format(source3))
    fo.write('Statecode: {}\n'.format(statecode))
    fo.write('Station: {}\n'.format(station))
    fo.write('Sunrise: {}\n'.format(sunrise))
    fo.write('Sunset: {}\n'.format(sunset))
    fo.write('temp: {}°C\n'.format(temp))
    fo.write('TimeZone: {}\n'.format(timezone))
    fo.write('Ts: {}\n'.format(ts))
    fo.write('Ts2: {}\n'.format(ts2))
    fo.write('UVindex: {}\n'.format(uv))
    fo.write('Visibility: {}Km\n'.format(vis))
    fo.write('Description: {}\n'.format(desc))
    fo.write('Code: {}\n'.format(code))
    fo.write('Icon: {}\n'.format(icon))
    fo.write('Winddegabb: {}\n'.format(winddegabb))
    fo.write('Winddegverb: {}\n'.format(winddegverb))
    fo.write('Winddeg: {}\n'.format(winddeg))
    fo.write('Windspeed: {} Km/h\n'.format(windspeed))
    fo.close()
    ################################ write clean data on a file
    fo = open(ptodayclean, 'w')
    fo.write('{}\n'.format(count))
    fo.write('{}\n'.format(tempfeelslike))
    fo.write('{}\n'.format(aqi))
    fo.write('{}\n'.format(cityname))
    fo.write('{}\n'.format(clouds))
    fo.write('{}\n'.format(countrycode))
    fo.write('{}\n'.format(datetimec))
    fo.write('{}\n'.format(cdewpoint))
    fo.write('{}\n'.format(dhi))
    fo.write('{}\n'.format(dni))
    fo.write('{}\n'.format(elevangle))
    fo.write('{}\n'.format(ghi))
    fo.write('{}\n'.format(windgust))
    fo.write('{}\n'.format(hangle))
    fo.write('{}\n'.format(lat))
    fo.write('{}\n'.format(lon))
    fo.write('{}\n'.format(obtime))
    fo.write('{}\n'.format(pod))
    fo.write('{}\n'.format(precip))
    fo.write('{}\n'.format(pressure))
    fo.write('{}\n'.format(humidity))
    fo.write('{}\n'.format(seapressure))
    fo.write('{}\n'.format(snow))
    fo.write('{}\n'.format(solarrad))
    fo.write('{}\n'.format(source0))
    fo.write('{}\n'.format(source1))
    fo.write('{}\n'.format(source2))
    fo.write('{}\n'.format(source3))
    fo.write('{}\n'.format(statecode))
    fo.write('{}\n'.format(station))
    fo.write('{}\n'.format(sunrise))
    fo.write('{}\n'.format(sunset))
    fo.write('{}\n'.format(temp))
    fo.write('{}\n'.format(timezone))
    fo.write('{}\n'.format(ts))
    fo.write('{}\n'.format(ts2))
    fo.write('{}\n'.format(uv))
    fo.write('{}\n'.format(vis))
    fo.write('{}\n'.format(desc))
    fo.write('{}\n'.format(code))
    fo.write('{}\n'.format(icon))
    fo.write('{}\n'.format(winddegabb))
    fo.write('{}\n'.format(winddegverb))
    fo.write('{}\n'.format(winddeg))
    fo.write('{}\n'.format(windspeed))
    fo.close()
    ################################ create FLAG path
    pi = "${image " + home
    pi2 = homename
    pi3 = conky + 'flags/'
    pf = '.png -p 381,0 -s 19x13}'
    countrycode = countrycode.lower()
    tot = pi + pi2 + pi3 + countrycode + pf
    if countrycode == vtext:
       fo = open(pflags, 'w')
       tot = 'transparent'
       fo.write('{}\n'.format(tot))
    elif countrycode != vtext:
       fo = open(pflags, 'w')
       fo.write('{}\n'.format(tot))
    fo.close()
    ################################ create the path for weatherbit logo
    pi = "${image " + home
    pi2 = homename
    pi3 = conky + 'weather/Weatherbit/wblogo2'
    est = '.png -p '
    x = 110
    virg = ','
    y = 0
    pf = ' -s 15x15}'
    fo = open(pwblogo, 'w')
    tot = pi + pi2 + pi3 + est + str(x) + virg + str(y) + pf
    fo.write('{}\n'.format(tot))
    fo.close()
    ################################ write the path for COMPASS icon
    #                  grades calculation for winddeg, trasparent image if no wind (use negative tdeg to rotate clockwise)
    if winddeg == 'empty':
        tdeg = myd
        temp1 = Image.open(parrowt)
        temp2 = temp1.rotate(-tdeg)    
        temp2.save(parrowt2)
        temp3 = '${image ' + home
        temp4 = homename
        temp5 = conky + 'weather/compass/arrowt2'
        pfcomp = '.png -p 305,60 -s 100x100}'
        totcomp = temp3 + temp4 + temp5 + pfcomp
        fo = open(pcompass, 'w')
        fo.write('{}\n'.format(totcomp))
        fo.write('{}\n'.format(pathwindrose))
    elif winddeg != 'empty':
        tdeg = myd + winddeg
        temp1 = Image.open(parrow)
        temp2 = temp1.rotate(-tdeg)
        temp2.save(parrow2)
        temp3 = '${image ' + home
        temp4 = homename
        temp5 = conky + 'weather/compass/arrow2'
        pfcomp = '.png -p 305,60 -s 100x100}'
        totcomp = temp3 + temp4 + temp5 + pfcomp
        fo = open(pcompass, 'w')
        fo.write('{}\n'.format(totcomp))
        fo.write('{}\n'.format(pathwindrose))
    fo.close()
    ################################ calculate dew point and write it
    dpc = cdewpoint
    color = 'white'
    #                  calculate the DEW POINT color font based on index
    if (dpc < 19):
        color = 6
    elif (dpc >=19 and dpc < 22):
        color = 9
    elif (dpc >=22):
        color = 4
    else:
        color = 'white'
    fo = open(pdewpoint, 'w')
    fo.write('{}\n'.format(cdewpoint))
    fo.write('{}\n'.format(color))
    fo.close()
    ################################ calculate today UV index color and write it
    value = uv
    if (value >=0 and value < 3):
        color = 6
    elif (value >=3 and value < 6):
        color = 9
    elif (value >=6 and value < 8):
        color = 3
    elif (value >=8 and value < 11):
        color = 4
    elif (value >= 11):
        color = 0
    else:
        color = 2
    fo = open(puvindex, 'w')
    fo.write('{}\n'.format(value))
    fo.write('{}\n'.format(color))
    fo.close()
    ################################ calculate today AQI color and write it
    value = aqi
    if (value >=0 and value < 51):
        color = 6
    elif (value >=51 and value < 101):
        color = 9
    elif (value >=101 and value < 151):
        color = 3
    elif (value >=151 and value < 200):
        color = 4
    elif (value >=201 and value < 300):
        color = 0
    elif (value >=301):
        color = 1
    fo = open(paqi, 'w')
    fo.write('{}\n'.format(value))
    fo.write('{}\n'.format(color))
    fo.close()
    ################################ write main icon path
    pi = '${image ' + home
    pi2 = homename
    pi3 = conky + 'weather/Weatherbit/icons/'
    icontemp = pod
    pf = '.png -p 0,30 -s 120x120}'
    tot = pi + pi2 + pi3 + str(icon) + pf
    if icontemp == 'd':
       fo = open(ptodaymainicon, 'w')
       fo.write('{}\n'.format(tot))
    elif icontemp == 'n':
       fo = open(ptodaymainicon, 'w')
       fo.write('{}\n'.format(tot))
    fo.close()
    ################################ write icon HOT path
    if tempfeelslike >= 38:
       pi = '${image ' + home
       pi2 = homename
       pi3 = conky + 'weather/Weatherbit/icons/'
       temp = 'hot'
       pf = '.png -p 240,70 -s 85x51}'
       tot = pi + pi2 + pi3 + temp + pf
       fo = open(photicon, 'w')
       fo.write('{}\n'.format(tot))
       fo.close()
    else:
       temp = 'transparent'
       pf = '.png -p 240,70 -s 85x51}'
       tot = pi + pi2 + pi3 + temp + pf
       fo = open(photicon, 'w')
       fo.write('{}\n'.format(tot))
       fo.close()
    ################################ write icon COLD path
    if tempfeelslike <= 0:
       pi = '${image ' + home
       pi2 = homename
       pi3 = conky + 'weather/Weatherbit/icons/'
       temp = 'cold'
       pf = '.png -p 240,70 -s 85x51}'
       tot = pi + pi2 + pi3 + temp + pf
       fo = open(pcoldicon, 'w')
       fo.write('{}\n'.format(tot))
       fo.close()
    else:
       temp = 'transparent'
       pf = '.png -p 240,70 -s 85x51}'
       tot = pi + pi2 + pi3 + temp + pf
       fo = open(pcoldicon, 'w')
       fo.write('{}\n'.format(tot))
       fo.close()
    ################################ create CURRENT, section
    #                 main CURRENT in todayconky.txt
    pathtemp = "$HOME" + conky + "weather/Weatherbit/today/"
    pathtemp2 = "$HOME" + conky + "weather/Weatherbit/"
    wbpylogo = '${image ' + pathtemp2 + 'python_logo.png -p 130,0 -s 15x15}'
    infotz = "${color2}${font = 'URW Gothic L:size=8'}WEATHERBIT    ${font}${color1}${alignr}${execpi 900 sed -n '34p' " + pathtemp + "wbtodayraw.txt}"
    infotzerr = "${color2}${font = 'URW Gothic L:size=8'}WEATHERBIT     ${color4}E: " + coderr + "${font}${color1}${alignr}${execpi 900 sed -n '34p' " + pathtemp + "wbtodayraw.txt}"
    latlon = "${alignr}(${execpi 900 sed -n '15p' " + pathtemp + "wbtodayraw.txt} - ${execpi 900 sed -n '16p' " + pathtemp + "wbtodayraw.txt})${font}${color}"
    curricon = "${execpi 900 sed -n '1p' " + pathtemp + "todayicon.txt}"
    firstdesc = "${color4}${goto 190}${execpi 900 sed -n '39p' " + pathtemp + "wbtodayclean.txt}${color}"
    currtemp = "${color}${goto 190}temp: ${execpi 900 sed -n '33p' " + pathtemp + "wbtodayclean.txt}${color}°C"
    currtempf = "${goto 190}(feel: ${execpi 900 sed -n '2p' " + pathtemp + "wbtodayclean.txt}°C)"
    thermo = "${execpi 900 sed -n '1p' " + pathtemp + "todayiconhotOWM.txt}${execpi 900 sed -n '1p' " + pathtemp + "todayiconcoldOWM.txt}"
    raininfo = "${color}${goto 190}rain/h: ${execpi 900 sed -n '19p' " + pathtemp + "wbtodayclean.txt}mm"
    snowinfo = "${color}${goto 190}snow/h: ${execpi 900 sed -n '23p' " + pathtemp + "wbtodayclean.txt}mm"
    winds = "${color}${goto 190}wind speed: ${execpi 900 sed -n '45p' " + pathtemp + "wbtodayclean.txt} Km/h"
    windg = "${color}${goto 190}wind gust: ${execpi 900 sed -n '13p' " + pathtemp + "wbtodayclean.txt} Km/h"
    info1 = "${color2}HUMIDITY: $color${execpi 900 sed -n '21p' " + pathtemp + "wbtodayclean.txt}%${goto 260}${color2}PRESSURE: $color${execpi 900 sed -n '20p' " + pathtemp + "wbtodayclean.txt}mb"
    info2 = "${color2}UV INDEX (${color6}0${color2}-${color0}11+${color2}): ${eval $${color${execpi 900 sed -n '2p' " + pathtemp + "todaywbuvindex.txt}}}${execpi 900 sed -n '1p' " + pathtemp + "todaywbuvindex.txt}${goto 260}${color2}SEA PRESSURE: $color${execpi 900 sed -n '22p' " + pathtemp + "wbtodayclean.txt}mb"
    info3 = "${color2}DEW POINT: ${eval $${color${execpi 900 sed -n '2p' " + pathtemp + "todaywbdewpoint.txt}}}${execpi 900 sed -n '1p' " + pathtemp + "todaywbdewpoint.txt}${color}°C${color2}${goto 260}VISIBILITY: $color${execpi 900 sed -n '38p' " + pathtemp + "wbtodayclean.txt} Km"
    info4 = "${color2}CLOUDS COVER: $color${execpi 900 sed -n '5p' " + pathtemp + "wbtodayclean.txt}%${goto 260}${color2}AQI (${color6}0${color2}-${color8}500${color2}): ${eval $${color${execpi 900 sed -n '2p' " + pathtemp + "todaywbaqi.txt}}}${execpi 900 sed -n '1p' " + pathtemp + "todaywbaqi.txt}"
    info5= "${color2}SUNRISE: $color${execpi 900 sed -n '31p' " + pathtemp + "wbtodayclean.txt}${color2}${goto 260}SUNSET: $color${execpi 900 sed -n '32p' " + pathtemp + "wbtodayclean.txt}${color}"
    #info6= "${color2}RAIN: $color${execpi 900 sed -n '19p' " + pathtemp + "wbtodayclean.txt}mm/hr${color2}${goto 260}SNOW: $color${execpi 900 sed -n '23p' " + pathtemp + "wbtodayclean.txt}mm/hr${color}"
    info6= "${color2}SOLAR RAD: $color${execpi 900 sed -n '24p' " + pathtemp + "wbtodayclean.txt} W/m^2${color2}${goto 260}DHI: $color${execpi 900 sed -n '9p' " + pathtemp + "wbtodayclean.txt} W/m^2${color}"
    info7= "${color2}SOLAR ELEV ANGLE: $color${execpi 900 sed -n '11p' " + pathtemp + "wbtodayclean.txt}°${color2}${goto 260}DNI: $color${execpi 900 sed -n '10p' " + pathtemp + "wbtodayclean.txt} W/m^2${color}"
    info8= "${color2}SOLAR HOUR ANGLE: $color${execpi 900 sed -n '14p' " + pathtemp + "wbtodayclean.txt}°${color2}${goto 260}GHI: $color${execpi 900 sed -n '12p' " + pathtemp + "wbtodayclean.txt} W/m^2${color}"
    #dashedline = '---------------------------------------------------------------------------------------------------------'
    fo = open(pathtodayconky, 'w')
    if coderr != 'ok':
        fo.write('{}\n'.format(wbpylogo + infotzerr))
    else:
        fo.write('{}\n'.format(wbpylogo + infotz))
    fo.write('{}\n'.format(latlon))
    fo.write('{}\n'.format(firstdesc))
    fo.write('{}\n'.format(currtemp))
    fo.write('{}\n'.format(currtempf + thermo))
    fo.write('{}\n'.format(raininfo))
    fo.write('{}\n'.format(snowinfo))
    fo.write('{}\n'.format(winds))
    fo.write('{}\n'.format(info1))
    fo.write('{}\n'.format(info2))
    fo.write('{}\n'.format(info3))
    fo.write('{}\n'.format(info4))
    fo.write('{}\n'.format(info5))
    fo.write('{}\n'.format(info6))
    fo.write('{}\n'.format(info7))
    fo.write('{}\n'.format(info8))
    #fo.write('{}\n'.format(dashedline))
    fo.close()
except Exception as e:
    # Manage exceptions (optional)
    filelockerror = (f"Error during script execution: {e}")
finally:
    # remove lock file
    try:
        os.remove(lock_file)
    except FileNotFoundError:
        pass  # file already removed