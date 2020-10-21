# Ruckus Nagios Check for Virtual Smartzone and Access Points

This Nagios/Icinga Check provides the ability to query Ruckus Virtual Smartzone Gateway devices for current system status.
The plugin has been tested with SmartCell Gateway Versions 3.5 and 5.1.

It will check and generate performance data for:

- number of access points
- connected stations
- traffic statistics
- system load
- memory
- harddisk
- system uptime
 
In addition you can query performance data of the connected access points. 
 
## Dependencies

Implementation is in Python. You will need a installed Python interpreter and the following Python modules:
  
- nagiosplugin
- pysnmp
- configparser
- ipaddress (python3 backport)

## Manual installation on your Nagios Host
```Shell
pip install -r requirements.txt
python setup.py install
ln -s /usr/bin/check_ruckus_vsz /usr/lib/nagios/plugins/check_ruckus_vsz
ln -s /usr/bin/check_ruckus_ap /usr/lib/nagios/plugins/check_ruckus_ap # optional
```

## Installation Debian package

For Debian you can use the provided Debian package. Debian Jessie and above should be fine without any additional packages. 

## Usage example

Nagios Plugin called manually:

```Shell
./check_ruckus_vsz -H 10.0.0.1 -C public
```

See `check_ruckus_vsz -h` for additional command line arguments. Use -vvv to get Debug Output including additional system information.

## AccessPoint checks

This package also contains a check for single APs configured with the Virtual Smartzone Gateway.

Monitored AP zones and groups can be configured by using the `--zone-regex` and `--group-regex` command line options or corresponding configuration file statements. 
This defaults to `.*` which will included every approved AP.

This check returns performance data about single APs like transferred bytes and connected stations,
it sets it status to CRIT if the monitored AP is disconnected and WARN if there are unapplied configuration changes.

### Configuration AccessPoint checks

To configure these AP checks there is a special option `-o /path` on check_ruckus_vsz which can be used to set
an output directory for nagios host and service configuration files.

The script writes a configuration for every approved AP within the configured zones and groups,
using the hostname of the defined controller as "real" address and setting a hostname based on the
`--hostname-format` command line option.

The hostname format is a python formatted string with a few variables (mac[0] - mac[5], ip, ipv6, extip, name) set.  
An example config value could be `--hostname_format "ap-{mac[0]}{mac[1]}{mac[2]}{mac[3]}{mac[4]}{mac[5]}.ddns.example.org"`.

To write these configuration files to a directory add the `-o /path` parameter in a cronjob or similar (don't set this on your nagios check):

```Shell
./check_ruckus_vsz -H 10.0.0.1 -C public -o /etc/nagios3/ruckus.d
```

Make sure that the output dir exists and is included in your nagios configuration using the cfg_dir statement. 

## Using a config file

You can use a config file to change ranges of the warning and critical value ranges for the different monitored devices. 
The config file is expected to be named `/etc/check_ruckus_vsz.conf`. Using the command line switch `--config (-c)` you can override this behaviour.

The config file must contain sections named after the specified hostname/hostaddress of the device (parameter -H) of the check_ruckus_vsz call.
You can list the changed parameters within this section. Non present values will be set to default values.

Example with default values:

/etc/check_ruckus_vsz.conf

```
[10.0.0.1]
zone_regex = .*
group_regex = .*

data_free_min_warn = 40
data_free_min_crit = 30

mem_free_min_warn = 4
mem_free_min_crit = 2

load_1min_max_warn = 5.0
load_1min_max_crit = 10.0
load_5min_max_warn = 4.0
load_5min_max_crit = 6.0
load_15min_max_warn = 3.0
load_15min_max_crit = 4.0
```

## Nagios Integration

Define the commands for Nagios checks and include it in the service definitions:

```
define command {
	command_name	check_ruckus_vsz
	command_line	/usr/lib/nagios/plugins/check_ruckus_vsz -C $ARG1$ -H $HOSTADDRESS$
}
define service {
	use			generic-service-perfdata
	hostgroup_name		ruckus_vsz
	service_description	check_ruckus_vsz
	check_command		check_ruckus_vsz!SNMP_COMMUNITY
}

# optional ap check command
define command {
	command_name	check_ruckus_ap
	command_line	/usr/lib/nagios/plugins/check_ruckus_ap -C $ARG1$ -H $HOSTADDRESS$ -a $ARG2$
}
```
