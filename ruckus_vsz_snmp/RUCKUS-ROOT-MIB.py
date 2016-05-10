# PySNMP SMI module. Autogenerated from smidump -f python RUCKUS-ROOT-MIB
# by libsmi2pysnmp-0.1.3 at Thu May 19 15:23:57 2016,
# Python version sys.version_info(major=2, minor=7, micro=11, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( Bits, Integer32, ModuleIdentity, MibIdentifier, TimeTicks, enterprises, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "MibIdentifier", "TimeTicks", "enterprises")

# Objects

ruckusRootMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 25053)).setRevisions(("2014-05-19 11:00",))
if mibBuilder.loadTexts: ruckusRootMIB.setOrganization("Ruckus Wireless, Inc.")
if mibBuilder.loadTexts: ruckusRootMIB.setContactInfo("Ruckus Wireless, Inc.\n\n350 West Java Dr.\nSunnyvale, CA 94089\nUSA\n\nT: +1 (650) 265-4200\nF: +1 (408) 738-2065\nEMail: info@ruckuswireless.com\nWeb: www.ruckuswireless.com")
if mibBuilder.loadTexts: ruckusRootMIB.setDescription("Ruckus top level mib.")
ruckusObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1))
ruckusCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1))
ruckusCommonTCModule = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 1))
ruckusZD = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 2))
ruckusZDSystemModule = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 2, 1))
ruckusZDWLANModule = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 2, 2))
ruckusSCG = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 3))
ruckusSCGSystemModule = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 3, 1))
ruckusSCGWLANModule = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 3, 2))
ruckusSCGTTGModule = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 3, 3))
ruckusSZ = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 4))
ruckusSZSystemModule = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 4, 1))
ruckusSZWLANModule = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 4, 2))
ruckusEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 2))
ruckusProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 3))

# Augmentions

# Exports

# Module identity
mibBuilder.exportSymbols("RUCKUS-ROOT-MIB", PYSNMP_MODULE_ID=ruckusRootMIB)

# Objects
mibBuilder.exportSymbols("RUCKUS-ROOT-MIB", ruckusRootMIB=ruckusRootMIB, ruckusObjects=ruckusObjects, ruckusCommon=ruckusCommon, ruckusCommonTCModule=ruckusCommonTCModule, ruckusZD=ruckusZD, ruckusZDSystemModule=ruckusZDSystemModule, ruckusZDWLANModule=ruckusZDWLANModule, ruckusSCG=ruckusSCG, ruckusSCGSystemModule=ruckusSCGSystemModule, ruckusSCGWLANModule=ruckusSCGWLANModule, ruckusSCGTTGModule=ruckusSCGTTGModule, ruckusSZ=ruckusSZ, ruckusSZSystemModule=ruckusSZSystemModule, ruckusSZWLANModule=ruckusSZWLANModule, ruckusEvents=ruckusEvents, ruckusProducts=ruckusProducts)

