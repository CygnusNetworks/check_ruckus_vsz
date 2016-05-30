<?php

$def[1] = '';
$def[2] = '';

for ($i=1; $i <= count($DS); $i++) {
  switch($NAME[$i]) {
    case 'num_sta': $def[1] .= rrd::def($NAME[$i], $RRDFILE[1], $DS[$i]); break;
    case 'stats_rx_bytes': $def[2] .= rrd::def($NAME[$i], $RRDFILE[1], $DS[$i]); break;
    case 'stats_tx_bytes': $def[2] .= rrd::def($NAME[$i], $RRDFILE[1], $DS[$i]); break;
    default: break;
  }
}

$ds_name[1] = 'Clients';
$opt[1] = "--upper-limit 42 --lower-limit 0 --vertical-label \"Clients\"  --title $hostname";
$def[1] .= rrd::line1("num_sta", "#21db2a", "Number of Clients");
$def[1] .= rrd::gprint("num_sta", array("LAST", "AVERAGE", "MAX"), "Average %3.0lf");

$ds_name[2] = 'Throughput';
$opt[2] = "--upper-limit 250 --lower-limit 0 --vertical-label \"Bytes\"  --title $hostname";
$def[2] .= rrd::line1("stats_rx_bytes", "#21db2a", "Received Bytes");
$def[2] .= rrd::gprint("stats_rx_bytes", array("LAST", "AVERAGE", "MAX"), "%3.0lf");

$def[2] .= rrd::line1("stats_tx_bytes", "#db212a", "Transmitted Bytes");
$def[2] .= rrd::gprint("stats_tx_bytes", array("LAST", "AVERAGE", "MAX"), "%3.0lf");

?>
