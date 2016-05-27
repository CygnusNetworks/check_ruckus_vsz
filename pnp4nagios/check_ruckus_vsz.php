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
$opt[1] = "--upper-limit 250 --lower-limit 0 --vertical-label \"Clients\"  --title $hostname";
$def[1] .= rrd::line1("num_sta", "#21db2a", "Number of Clients");
$def[1] .= rrd::gprint("num_sta", "AVERAGE", "Average %3.0lf");
$def[1] .= rrd::gprint("num_sta", "MAX", "Max %3.0lf");
$def[1] .= rrd::gprint("num_sta", "LAST", "Last %3.0lf\\n");

$ds_name[2] = 'Total Throughput';
$opt[2] = "--upper-limit 250 --lower-limit 0 --vertical-label \"Bytes\"  --title $hostname";
$def[2] .= rrd::line1("stats_rx_bytes", "#21db2a", "Received Bytes");
$def[2] .= rrd::gprint("stats_rx_bytes", array("LAST", "AVERAGE", "MAX"), "%3.0lf");

$def[2] .= rrd::line1("stats_tx_bytes", "#db212a", "Transmitted Bytes");
$def[2] .= rrd::gprint("stats_tx_bytes", array("LAST", "AVERAGE", "MAX"), "%3.0lf");

$scgaps = array();
for ($i=1; $i <= count($DS); $i++) {
  if(preg_match("/^scgap_([A-Z0-9]{12})_/", $NAME[$i], $matches)) {
    $scgap_name = $matches[1];
    if(array_key_exists($scgap_name, $scgaps)) {
      $defid = $scgaps[$scgap_name];
    } else {
      $defid = count($def) + 1;
      $scgaps[$scgap_name] = $defid;
      $def[$defid] = '';
      $ds_name[$defid] = 'AP '.preg_replace('/..(?!$)/', '$0:', $scgap_name);
      $opt[$defid] = "--upper-limit 100 --lower-limit 0 --vertical-label \"Stuff\"  --title $hostname";
    }

    switch(preg_replace('/^scgap_[A-Z0-9]{12}_/', '', $NAME[$i])) {
      case 'rx_bytes':
        $def[$defid] .= rrd::def($NAME[$i], $RRDFILE[1], $DS[$i]);
        $def[$defid] .= rrd::line1($NAME[$i], "#21db2a", "Received Bytes");
        $def[$defid] .= rrd::gprint($NAME[$i], array("LAST", "AVERAGE", "MAX"), "%3.0lf");
        break;
      case 'tx_bytes':
        $def[$defid] .= rrd::def($NAME[$i], $RRDFILE[1], $DS[$i]);
        $def[$defid] .= rrd::line1($NAME[$i], "#db212a", "Transmitted Bytes");
        $def[$defid] .= rrd::gprint($NAME[$i], array("LAST", "AVERAGE", "MAX"), "%3.0lf");
        break;
      case 'numsta':
        $def[$defid] .= rrd::def($NAME[$i], $RRDFILE[1], $DS[$i]);
        $def[$defid] .= rrd::line1($NAME[$i], "#2a21db", "Clients");
        $def[$defid] .= rrd::gprint($NAME[$i], array("LAST", "AVERAGE", "MAX"), "%3.0lf");
        break;
      default: break;
    }
  }
}

?>
