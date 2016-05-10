# PySNMP SMI module. Autogenerated from smidump -f python RUCKUS-PRODUCTS-MIB
# by libsmi2pysnmp-0.1.3 at Thu May 19 15:23:57 2016,
# Python version sys.version_info(major=2, minor=7, micro=11, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( ifIndex, ) = mibBuilder.importSymbols("IF-MIB", "ifIndex")
( IpAddress, ) = mibBuilder.importSymbols("RFC1155-SMI", "IpAddress")
( ruckusProducts, ) = mibBuilder.importSymbols("RUCKUS-ROOT-MIB", "ruckusProducts")
( RuckusCountryCode, ) = mibBuilder.importSymbols("RUCKUS-TC-MIB", "RuckusCountryCode")
( Bits, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32")
( DisplayString, MacAddress, TruthValue, ) = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TruthValue")

# Objects

ruckusProductsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 25053, 3, 1)).setRevisions(("2014-05-19 11:00",))
if mibBuilder.loadTexts: ruckusProductsMIB.setOrganization("Ruckus Wireless, Inc.")
if mibBuilder.loadTexts: ruckusProductsMIB.setContactInfo("Ruckus Wireless, Inc.\n\n350 West Java Dr.\nSunnyvale, CA 94089\nUSA\n\nT: +1 (650) 265-4200\nF: +1 (408) 738-2065\nEMail: info@ruckuswireless.com\nWeb: www.ruckuswireless.com")
if mibBuilder.loadTexts: ruckusProductsMIB.setDescription("Ruckus product OID registration mib.")
ruckusWirelessRouterProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 1))
ruckusVF2825 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 1, 1))
ruckusVF2811 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 1, 2))
ruckusVF2821 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 1, 3))
ruckusVF2835 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 1, 4))
ruckusVF7811 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 1, 5))
ruckusWirelessAdapterProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 2))
ruckusVF2111 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 2, 1))
ruckusVF2121 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 2, 2))
ruckusVF7111 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 2, 3))
ruckusWirelessMetroProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 3))
ruckusMM2225 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 3, 1))
ruckusMM2211 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 3, 2))
ruckusMM2221 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 3, 3))
ruckusWirelessHotzoneProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4))
ruckusZF2925 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 1))
ruckusZF2942 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 2))
ruckusZF7942 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 3))
ruckusZF7962 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 4))
ruckusZF2741 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 5))
ruckusZF7762 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 6))
ruckusZF7761CM = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 7))
ruckusZF7761CMControlLED = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 7, 3), Integer().subtype(subtypeSpec=SingleValueConstraint(5,6,15,10,4,3,1,8,9,2,11,13,7,12,14,)).subtype(namedValues=NamedValues(("ledPerCM", 1), ("softResetAP", 10), ("powerCycleAP", 11), ("factoryResetAP", 12), ("softResetCM", 13), ("powerCycleCM", 14), ("factoryResetCM", 15), ("ledPerAP", 2), ("ledAlternateMode1Mode2OneHour", 3), ("ledAlternateMode1Mode2Mode6", 4), ("blueActive", 5), ("blueActiveCMOnlineLed", 6), ("ledAllOff", 7), ("heartbeatOffCM", 8), ("heartbeatOffAP", 9), )).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZF7761CMControlLED.setDescription("ledPerCM(1):                      LEDs enabled per Cable Modem definition,\nledPerAP(2):                      LEDs configured per Access Point definition,\nledAlternateMode1Mode2OneHour(3): Alternalte between modes 1 and 2 at a 30 second period then disabled after one hour,\nledAlternateMode1Mode2Mode6(4):   Alternalte between modes 1 and 2 at a 30 second period and then go to mode 6\nblueActive(5):                    Blue Active Surge Protection Indicator,\nblueActiveCMOnlineLed(6):         Blue Active Surge Protection Indicator and Cable Modem online Green LED enabled,\nledAllOff(7):                     All LEDs disabled,\nheartbeatOffCM(8):                Disable Cable Modem heartbeat monitoring,\nheartbeatOffAP(9):                Disable Access Point heartbeat monitoring,\nsoftResetAP(10):                  Soft reset of Access Point,\npowerCycleAP(11):                 Power cycle Access Point,\nfactoryResetAP(12):               Reset Access Point to factory defaults,\nsoftResetCM(13):                  Soft reset of Cable Modem,\npowerCycleCM(14):                 Power cycle Cable Modem,\nfactoryResetCM(15):               Reset Cable Modem to factory defaults")
ruckusZF7761CMWanIPAddr = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 7, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZF7761CMWanIPAddr.setDescription("Specifies the IP address of the Cable Modem WAN interface.")
ruckusZF7761CMCustomization = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 7, 5))
ruckusZF7761CMHTTPService = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 7, 5, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZF7761CMHTTPService.setDescription("Enable/disable HTTP service.")
ruckusZF7761CMTelnetService = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 7, 5, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZF7761CMTelnetService.setDescription("Enable/disable Telnet service.")
ruckusZF7761CMSSHService = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 7, 5, 3), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZF7761CMSSHService.setDescription("Enable/disable SSH service.")
ruckusZF7761CMUsername = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 7, 5, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZF7761CMUsername.setDescription("Specifies username of cable modem. ")
ruckusZF7761CMPassword = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 7, 5, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZF7761CMPassword.setDescription("Specifies password of cable modem. ")
ruckusZF7761CMLEDMode = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 7, 6), Integer().subtype(subtypeSpec=SingleValueConstraint(1,0,2,)).subtype(namedValues=NamedValues(("ledAllOff", 0), ("blueActive", 1), ("blueActiveCMOnlineLed", 2), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZF7761CMLEDMode.setDescription("ledAllOff(0):               All LEDs disabled after 3 second delay,\nblueActive(1):              Blue Active Surge Protection Indicator,\nblueActiveCMOnlineLed(2):   Blue Active Surge Protection Indicator and Cable Modem online Green LED enabled")
ruckusZF7761CMHeartbeatMonitorCM = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 7, 7), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZF7761CMHeartbeatMonitorCM.setDescription("Enable/disable Cable Modem heartbeat monitoring.")
ruckusZF7761CMHeartbeatMonitorAP = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 7, 8), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusZF7761CMHeartbeatMonitorAP.setDescription("Enable/disable Access Point heartbeat monitoring.")
ruckusZF7762S = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 8))
ruckusZF7762T = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 9))
ruckusZF7762N = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 10))
ruckusZF7343 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 12))
ruckusZF7363 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 13))
ruckusZF7341 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 14))
ruckusZF7731 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 16))
ruckusZF7025 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 20))
ruckusZF7321 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 22))
ruckusZF7321U = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 23))
ruckusZF2741EXT = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 24))
ruckusZF7982 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 25))
ruckusZF7782 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 28))
ruckusZF7782S = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 29))
ruckusZF7782N = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 30))
ruckusZF7782E = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 31))
ruckusZF8800SAC = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 32))
ruckusZF7762AC = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 35))
ruckusZF7762SAC = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 36))
ruckusZF7762TAC = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 37))
ruckusZF7372 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 40))
ruckusZF7372E = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 41))
ruckusZF7441 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 42))
ruckusZF7352 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 45))
ruckusZF7351 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 48))
ruckusZF7742 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 50))
ruckusZF7055 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 52))
ruckusZF7781M = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 55))
ruckusZF7781CM = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 56))
ruckusZF7781CME = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 57))
ruckusZF7781CMS = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 58))
ruckusZF7781FN = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 60))
ruckusZF7781FNE = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 61))
ruckusZF7781FNS = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 62))
ruckusSC8800SAC = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 65))
ruckusSC8800S = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 66))
ruckusR300 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 67))
ruckusR310 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 68))
ruckusR700 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 69))
ruckusR710 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 70))
ruckusR500 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 71))
ruckusR600 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 72))
ruckusT300 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 74))
ruckusT300E = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 75))
ruckusT301N = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 76))
ruckusT301S = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 77))
ruckusT504 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 78))
ruckusH500 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 79))
ruckusC500 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 80))
ruckusP300 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 81))
ruckusFZM300 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 85))
ruckusFZP300 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 4, 86))
ruckusWirelessControllerProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5))
ruckusZD1000 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 1))
ruckusZD1000SystemName = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD1000SystemName.setDescription("System name")
ruckusZD1000SystemIPAddr = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD1000SystemIPAddr.setDescription("IP Address")
ruckusZD1000SystemMacAddr = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD1000SystemMacAddr.setDescription("MAC Address")
ruckusZD1000SystemUptime = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD1000SystemUptime.setDescription("Up time")
ruckusZD1000SystemModel = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD1000SystemModel.setDescription("Model")
ruckusZD1000SystemLicensedAPs = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD1000SystemLicensedAPs.setDescription("Licensed APs")
ruckusZD1000SystemSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD1000SystemSerialNumber.setDescription("Serial number")
ruckusZD1000SystemVersion = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD1000SystemVersion.setDescription("Software version")
ruckusZD1000CountryCode = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 1, 9), RuckusCountryCode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD1000CountryCode.setDescription("Country code")
ruckusZD1100 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 2))
ruckusZD1100SystemName = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 2, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD1100SystemName.setDescription("System name")
ruckusZD1100SystemIPAddr = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 2, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD1100SystemIPAddr.setDescription("IP Address")
ruckusZD1100SystemMacAddr = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 2, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD1100SystemMacAddr.setDescription("MAC Address")
ruckusZD1100SystemUptime = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 2, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD1100SystemUptime.setDescription("Up time")
ruckusZD1100SystemModel = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 2, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD1100SystemModel.setDescription("Model")
ruckusZD1100SystemLicensedAPs = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 2, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD1100SystemLicensedAPs.setDescription("Licensed APs")
ruckusZD1100SystemSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 2, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD1100SystemSerialNumber.setDescription("Serial number")
ruckusZD1100SystemVersion = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 2, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD1100SystemVersion.setDescription("Software version")
ruckusZD1100CountryCode = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 2, 9), RuckusCountryCode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD1100CountryCode.setDescription("Country code")
ruckusZD3000 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 3))
ruckusZD3000SystemName = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 3, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD3000SystemName.setDescription("System name")
ruckusZD3000SystemIPAddr = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 3, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD3000SystemIPAddr.setDescription("IP Address")
ruckusZD3000SystemMacAddr = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 3, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD3000SystemMacAddr.setDescription("MAC Address")
ruckusZD3000SystemUptime = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 3, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD3000SystemUptime.setDescription("Up time")
ruckusZD3000SystemModel = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 3, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD3000SystemModel.setDescription("Model")
ruckusZD3000SystemLicensedAPs = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 3, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD3000SystemLicensedAPs.setDescription("Licensed APs")
ruckusZD3000SystemSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 3, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD3000SystemSerialNumber.setDescription("Serial number")
ruckusZD3000SystemVersion = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 3, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD3000SystemVersion.setDescription("Software version")
ruckusZD3000CountryCode = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 3, 9), RuckusCountryCode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD3000CountryCode.setDescription("Country code")
ruckusZD5000 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 8))
ruckusZD5000SystemName = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 8, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD5000SystemName.setDescription("System name")
ruckusZD5000SystemIPAddr = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 8, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD5000SystemIPAddr.setDescription("IP Address")
ruckusZD5000SystemMacAddr = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 8, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD5000SystemMacAddr.setDescription("MAC Address")
ruckusZD5000SystemUptime = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 8, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD5000SystemUptime.setDescription("Up time")
ruckusZD5000SystemModel = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 8, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD5000SystemModel.setDescription("Model")
ruckusZD5000SystemLicensedAPs = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 8, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD5000SystemLicensedAPs.setDescription("Licensed APs")
ruckusZD5000SystemSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 8, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD5000SystemSerialNumber.setDescription("Serial number")
ruckusZD5000SystemVersion = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 8, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD5000SystemVersion.setDescription("Software version")
ruckusZD5000CountryCode = MibScalar((1, 3, 6, 1, 4, 1, 25053, 3, 1, 5, 8, 9), RuckusCountryCode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusZD5000CountryCode.setDescription("Country code")
ruckusWirelessSmartCellGatewayProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 10))
ruckusSCG200 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 10, 1))
ruckusWirelessSmartZoneProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 11))
ruckusSZ100 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 11, 1))
ruckusSZ50 = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3, 1, 11, 2))

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("RUCKUS-PRODUCTS-MIB", PYSNMP_MODULE_ID=ruckusProductsMIB)

# Objects
mibBuilder.exportSymbols("RUCKUS-PRODUCTS-MIB", ruckusProductsMIB=ruckusProductsMIB, ruckusWirelessRouterProducts=ruckusWirelessRouterProducts, ruckusVF2825=ruckusVF2825, ruckusVF2811=ruckusVF2811, ruckusVF2821=ruckusVF2821, ruckusVF2835=ruckusVF2835, ruckusVF7811=ruckusVF7811, ruckusWirelessAdapterProducts=ruckusWirelessAdapterProducts, ruckusVF2111=ruckusVF2111, ruckusVF2121=ruckusVF2121, ruckusVF7111=ruckusVF7111, ruckusWirelessMetroProducts=ruckusWirelessMetroProducts, ruckusMM2225=ruckusMM2225, ruckusMM2211=ruckusMM2211, ruckusMM2221=ruckusMM2221, ruckusWirelessHotzoneProducts=ruckusWirelessHotzoneProducts, ruckusZF2925=ruckusZF2925, ruckusZF2942=ruckusZF2942, ruckusZF7942=ruckusZF7942, ruckusZF7962=ruckusZF7962, ruckusZF2741=ruckusZF2741, ruckusZF7762=ruckusZF7762, ruckusZF7761CM=ruckusZF7761CM, ruckusZF7761CMControlLED=ruckusZF7761CMControlLED, ruckusZF7761CMWanIPAddr=ruckusZF7761CMWanIPAddr, ruckusZF7761CMCustomization=ruckusZF7761CMCustomization, ruckusZF7761CMHTTPService=ruckusZF7761CMHTTPService, ruckusZF7761CMTelnetService=ruckusZF7761CMTelnetService, ruckusZF7761CMSSHService=ruckusZF7761CMSSHService, ruckusZF7761CMUsername=ruckusZF7761CMUsername, ruckusZF7761CMPassword=ruckusZF7761CMPassword, ruckusZF7761CMLEDMode=ruckusZF7761CMLEDMode, ruckusZF7761CMHeartbeatMonitorCM=ruckusZF7761CMHeartbeatMonitorCM, ruckusZF7761CMHeartbeatMonitorAP=ruckusZF7761CMHeartbeatMonitorAP, ruckusZF7762S=ruckusZF7762S, ruckusZF7762T=ruckusZF7762T, ruckusZF7762N=ruckusZF7762N, ruckusZF7343=ruckusZF7343, ruckusZF7363=ruckusZF7363, ruckusZF7341=ruckusZF7341, ruckusZF7731=ruckusZF7731, ruckusZF7025=ruckusZF7025, ruckusZF7321=ruckusZF7321, ruckusZF7321U=ruckusZF7321U, ruckusZF2741EXT=ruckusZF2741EXT, ruckusZF7982=ruckusZF7982, ruckusZF7782=ruckusZF7782, ruckusZF7782S=ruckusZF7782S, ruckusZF7782N=ruckusZF7782N, ruckusZF7782E=ruckusZF7782E, ruckusZF8800SAC=ruckusZF8800SAC, ruckusZF7762AC=ruckusZF7762AC, ruckusZF7762SAC=ruckusZF7762SAC, ruckusZF7762TAC=ruckusZF7762TAC, ruckusZF7372=ruckusZF7372, ruckusZF7372E=ruckusZF7372E, ruckusZF7441=ruckusZF7441, ruckusZF7352=ruckusZF7352, ruckusZF7351=ruckusZF7351, ruckusZF7742=ruckusZF7742, ruckusZF7055=ruckusZF7055, ruckusZF7781M=ruckusZF7781M, ruckusZF7781CM=ruckusZF7781CM, ruckusZF7781CME=ruckusZF7781CME, ruckusZF7781CMS=ruckusZF7781CMS, ruckusZF7781FN=ruckusZF7781FN, ruckusZF7781FNE=ruckusZF7781FNE, ruckusZF7781FNS=ruckusZF7781FNS, ruckusSC8800SAC=ruckusSC8800SAC, ruckusSC8800S=ruckusSC8800S, ruckusR300=ruckusR300, ruckusR310=ruckusR310, ruckusR700=ruckusR700, ruckusR710=ruckusR710, ruckusR500=ruckusR500, ruckusR600=ruckusR600, ruckusT300=ruckusT300, ruckusT300E=ruckusT300E, ruckusT301N=ruckusT301N, ruckusT301S=ruckusT301S, ruckusT504=ruckusT504, ruckusH500=ruckusH500, ruckusC500=ruckusC500, ruckusP300=ruckusP300, ruckusFZM300=ruckusFZM300, ruckusFZP300=ruckusFZP300, ruckusWirelessControllerProducts=ruckusWirelessControllerProducts, ruckusZD1000=ruckusZD1000, ruckusZD1000SystemName=ruckusZD1000SystemName, ruckusZD1000SystemIPAddr=ruckusZD1000SystemIPAddr, ruckusZD1000SystemMacAddr=ruckusZD1000SystemMacAddr, ruckusZD1000SystemUptime=ruckusZD1000SystemUptime, ruckusZD1000SystemModel=ruckusZD1000SystemModel, ruckusZD1000SystemLicensedAPs=ruckusZD1000SystemLicensedAPs, ruckusZD1000SystemSerialNumber=ruckusZD1000SystemSerialNumber, ruckusZD1000SystemVersion=ruckusZD1000SystemVersion, ruckusZD1000CountryCode=ruckusZD1000CountryCode, ruckusZD1100=ruckusZD1100, ruckusZD1100SystemName=ruckusZD1100SystemName, ruckusZD1100SystemIPAddr=ruckusZD1100SystemIPAddr, ruckusZD1100SystemMacAddr=ruckusZD1100SystemMacAddr, ruckusZD1100SystemUptime=ruckusZD1100SystemUptime, ruckusZD1100SystemModel=ruckusZD1100SystemModel, ruckusZD1100SystemLicensedAPs=ruckusZD1100SystemLicensedAPs, ruckusZD1100SystemSerialNumber=ruckusZD1100SystemSerialNumber, ruckusZD1100SystemVersion=ruckusZD1100SystemVersion, ruckusZD1100CountryCode=ruckusZD1100CountryCode, ruckusZD3000=ruckusZD3000, ruckusZD3000SystemName=ruckusZD3000SystemName, ruckusZD3000SystemIPAddr=ruckusZD3000SystemIPAddr, ruckusZD3000SystemMacAddr=ruckusZD3000SystemMacAddr, ruckusZD3000SystemUptime=ruckusZD3000SystemUptime, ruckusZD3000SystemModel=ruckusZD3000SystemModel, ruckusZD3000SystemLicensedAPs=ruckusZD3000SystemLicensedAPs, ruckusZD3000SystemSerialNumber=ruckusZD3000SystemSerialNumber, ruckusZD3000SystemVersion=ruckusZD3000SystemVersion, ruckusZD3000CountryCode=ruckusZD3000CountryCode, ruckusZD5000=ruckusZD5000, ruckusZD5000SystemName=ruckusZD5000SystemName, ruckusZD5000SystemIPAddr=ruckusZD5000SystemIPAddr, ruckusZD5000SystemMacAddr=ruckusZD5000SystemMacAddr, ruckusZD5000SystemUptime=ruckusZD5000SystemUptime, ruckusZD5000SystemModel=ruckusZD5000SystemModel, ruckusZD5000SystemLicensedAPs=ruckusZD5000SystemLicensedAPs, ruckusZD5000SystemSerialNumber=ruckusZD5000SystemSerialNumber, ruckusZD5000SystemVersion=ruckusZD5000SystemVersion)
mibBuilder.exportSymbols("RUCKUS-PRODUCTS-MIB", ruckusZD5000CountryCode=ruckusZD5000CountryCode, ruckusWirelessSmartCellGatewayProducts=ruckusWirelessSmartCellGatewayProducts, ruckusSCG200=ruckusSCG200, ruckusWirelessSmartZoneProducts=ruckusWirelessSmartZoneProducts, ruckusSZ100=ruckusSZ100, ruckusSZ50=ruckusSZ50)

