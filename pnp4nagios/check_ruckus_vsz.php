<?php

$def[1] = '';
$def[2] = '';
$def[3] = '';
$def[4] = '';
$def[5] = '';

for ($i=1; $i <= count($DS); $i++) {
  switch($NAME[$i]) {
    case 'num_ap': $def[1] .= rrd::def($NAME[$i], $RRDFILE[1], $DS[$i]); break;
    case 'num_ap_connected': $def[1] .= rrd::def($NAME[$i], $RRDFILE[1], $DS[$i]); break;
    case 'num_ap_configured': $def[1] .= rrd::def($NAME[$i], $RRDFILE[1], $DS[$i]); break;
    case 'num_sta': $def[2] .= rrd::def($NAME[$i], $RRDFILE[1], $DS[$i]); break;
    case 'stats_rx_bytes': $def[3] .= rrd::def($NAME[$i], $RRDFILE[1], $DS[$i]); break;
    case 'stats_tx_bytes': $def[3] .= rrd::def($NAME[$i], $RRDFILE[1], $DS[$i]); break;
    case 'data_size': $def[4] .= rrd::def($NAME[$i], $RRDFILE[1], $DS[$i]); break;
    case 'data_free': $def[4] .= rrd::def($NAME[$i], $RRDFILE[1], $DS[$i]); break;
    case 'mem_size': $def[5] .= rrd::def($NAME[$i], $RRDFILE[1], $DS[$i]); break;
    case 'mem_free': $def[5] .= rrd::def($NAME[$i], $RRDFILE[1], $DS[$i]); break;
    default: break;
  }
}

$ds_name[1] = 'Access Points';
$opt[1] = "--lower-limit 0 --vertical-label \"Access Points\"  --title $hostname";
$def[1] .= rrd::line1("num_ap", "#21db2a", "Monitored accesspoints");
$def[1] .= rrd::gprint("num_ap", array("AVERAGE", "MAX", "LAST"), "%3.0lf");
$def[1] .= rrd::line1("num_ap_connected", "#db212a", "Connected accesspoints");
$def[1] .= rrd::gprint("num_ap_connected", array("AVERAGE", "MAX", "LAST"), "%3.0lf");
$def[1] .= rrd::line1("num_ap_configured", "#212adb", "Configured accesspoints");
$def[1] .= rrd::gprint("num_ap_configured", array("AVERAGE", "MAX", "LAST"), "%3.0lf");

$ds_name[2] = 'Clients';
$opt[2] = "--lower-limit 0 --vertical-label \"Clients\"  --title $hostname";
$def[2] .= rrd::line1("num_sta", "#21db2a", "Clients");
$def[2] .= rrd::gprint("num_sta", array("AVERAGE", "MAX", "LAST"), "%3.0lf");

$ds_name[3] = 'Total Throughput';
$opt[3] = "--lower-limit 0 --vertical-label \"Bytes\"  --title $hostname";
$def[3] .= rrd::line1("stats_rx_bytes", "#21db2a", "RX Bytes");
$def[3] .= rrd::gprint("stats_rx_bytes", array("AVERAGE", "MAX", "LAST"), "%3.2lf");

$def[3] .= rrd::line1("stats_tx_bytes", "#db212a", "TX Bytes");
$def[3] .= rrd::gprint("stats_tx_bytes", array("AVERAGE", "MAX", "LAST"), "%3.2lf");

$ds_name[4] = 'Data Partition';
$opt[4] = "--lower-limit 0 --vertical-label \"Bytes\"  --title $hostname";
$def[4] .= rrd::line1("data_size", "#21db2a", "Partition Size");
$def[4] .= rrd::gprint("data_size", array("AVERAGE", "MAX", "LAST"), "%3.2lf");

$def[4] .= rrd::line1("data_free", "#db212a", "Free Space");
$def[4] .= rrd::gprint("data_free", array("AVERAGE", "MAX", "LAST"), "%3.2lf");

$ds_name[5] = 'Memory';
$opt[5] = "--lower-limit 0 --vertical-label \"Bytes\"  --title $hostname";
$def[5] .= rrd::line1("mem_size", "#21db2a", "Total Memory");
$def[5] .= rrd::gprint("mem_size", array("AVERAGE", "MAX", "LAST"), "%3.2lf");

$def[5] .= rrd::line1("mem_free", "#db212a", "Free Memory");
$def[5] .= rrd::gprint("mem_free", array("AVERAGE", "MAX", "LAST"), "%3.2lf");

?>
