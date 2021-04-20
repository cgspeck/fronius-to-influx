# from https://review.solar/fronius-inverter-fault-codes/
error_codes = {
    -1: "test message",
    0: "",
    102: "The AC voltage is too high.",
    103: "The AC voltage is too low.",
    105: "The AC frequency is too high.",
    106: "The AC frequency is too low",
    301: "Excess AC current",
    302: "Excess DC current.",
    303: "DC module overheating.",
    304: "AC module overheating.",
    305: "Power is not being fed in, although the relay is closed.",
    306: "The PV output is too low to feed.",
    307: "The PV output is too low to feed.",
    308: "The intermediate circuit voltage is too high.",
    309: "The DC input voltage MPPT (maximum power point tracker) 1 is too high.",
    311: "The polarity of the DC strings reversed.",
    313: "The DC input voltage MPPT (maximum power point tracker) 2 is too high.",
    314: "Current sensor calibration timeout.",
    315: "AC current sensor error.",
    316: "Interrupt check fail.",
    317: "Unbalanced Intermediate circuit voltage.",
    318: "DC back current detected.",
    325: "Connection area overheating.",
    326: "Error with fan 1",
    327: "Error with fan 2",
    401: "The AC voltage is too high.",
    406: "Temperature sensor for AC module is faulty (L1)",
    407: "Temperature sensor for AC module is faulty (L2)",
    408: "DC component measured in the grid is too high.",
    412: "Fixed voltage mode has selected instead of MPP voltage mode and the fixed voltage mode has been set at the wrong value.",
    415: "Safety cut out has triggered via option card or RECERBO.",
    416: "Power stage set has no communication with control system.",
    417: "Hardware ID issue.",
    419: "Unique ID issue.",
    420: "Unable to communicate with hybrid manager.",
    421: "HID range error.",
    425: "Unable to communicate with power stage set.",
    426: "Hardware fault.",
    427: "Hardware fault.",
    428: "Hardware fault.",
    431: "Software fault.",
    436: "Functional incompatibility.",
    437: "Power stage fault.",
    438: "Functional incompatability.",
    443: "The intermediate circuit voltage is too low or asymmetric.",
    445: "Compatibility fault – Invalid power stage set configuration.",
    447: "Insulation problem.",
    448: "The neutral conducted is not connected.",
    450: "The guard can’t be found.",
    451: "Memory fault detected.",
    452: "Communication problem between processors.",
    453: "Power stage set and grid voltage are not compatible.",
    454: "Power stage set and grid frequency are not compatible.",
    456: "Anti-islanding function is no longer implemented correctly.",
    457: "The grid relay sticking or the neutral conductor ground voltage is too high.",
    458: "Issues when recording the measuring signal.",
    459: "Issues when recording the measuring signal for insulation test.",
    460: "Reference voltage source for the DSP (digital signal processor) is working out of tolerance.",
    461: "Error in the DSP (digital signal processor) data memory.",
    462: "Fault with the DC feed monitoring routine.",
    463: "Reversed AC polarity, The AC connector has been incorrectly inserted",
    474: "The RCMU sensor is faulty.",
    475: "Insulation fault (The connection between the solar panel and the ground is faulty)",
    476: "The driver supply voltage is too low.",
    479: "Intermediate circuit relay has switched off.",
    480: "Functional incompatibility (One or more PC boards in the inverter are not compatible together).",
    481: "Functional incompatibility (One or more PC boards in the inverter are not compatible together).",
    482: "The setup phase after the initial start-up was interrupted.",
    483: "The voltage UDC fixed on MPP2 string is out of limits.",
    485: "The CAN transmit buffer is full.",
    489: "Permanent intermediate circuit capacitor overvoltage.",
    502: "Insulation fault on the solar panels.",
    509: "No energy has been fed into the grid in the last 24 hours.",
    515: "Unable to communicate with filter.",
    516: "Unable to communicate with storage unit.",
    517: "Overheating which is causing power derating.",
    518: "Internal DSP fault.",
    519: "Unable to communicate with storage unit.",
    520: "No energy has been fed into the grid by MPPT1 in the past 24 hours.",
    522: "The DC is low in string 1.",
    523: "The DC is low in string 2.",
    528: "There is a functional incompatibility (one or more of the PC boards are not compatible).",
    529: "There is a functional incompatibility (one or more of the PC boards are not compatible).",
    560: "The grid frequency has become excessively high which is causing derating.",
    564: "There is a functional incompatibility (one or more of the PC boards are not compatible).",
    566: "The arc detector has been deactivated.",
    567: "The GVDPR (grid voltage depedent power reduction mode) is active and the inverter will operate with reduced power output.",
    601: "The CAN bus is full.",
    603: "The AC module sensor is faulty.",
    604: "The DC module sensor is faulty.",
    607: "RCMU fault.",
    608: "There is a functional incompatibility (one or more of the PC board are not compatible).",
    609: "Configuration Value Out of Limits .",
    701: "Information about the internal processors status.",
    702: "Information about the internal processors status.",
    703: "Information about the internal processors status.",
    704: "Information about the internal processors status.",
    705: "Information about the internal processors status.",
    706: "Information about the internal processors status.",
    707: "Information about the internal processors status.",
    708: "Information about the internal processors status.",
    709: "Information about the internal processors status.",
    710: "Information about the internal processors status.",
    711: "Information about the internal processors status.",
    712: "Information about the internal processors status.",
    713: "Information about the internal processors status.",
    714: "Information about the internal processors status.",
    715: "Information about the internal processors status.",
    716: "Information about the internal processors status.",
    721: "EEPROM has been re-initialised.",
    722: "Information about the internal processors status.",
    723: "Information about the internal processors status.",
    724: "Information about the internal processors status.",
    725: "Information about the internal processors status.",
    726: "Information about the internal processors status.",
    727: "Information about the internal processors status.",
    728: "Information about the internal processors status.",
    729: "Information about the internal processors status.",
    730: "Information about the internal processors status.",
    731: "USB flash drive not supported.",
    732: "Initialisation error with USB flash drive.",
    733: "USB flash drive not connected.",
    734: "Update file not recognised or missing.",
    735: "Update file is too old or does not match the device.",
    736: "Write or read error.",
    737: "Unable to open file.",
    738: "Unable to save log file.",
    740: "Error in file system on USB flash drive.",
    741: "Error recording logging data.",
    743: "Error during update.",
    745: "The update file is corrupt.",
    746: "Error while updating.",
    751: "Time lost.",
    752: "Communication error with real time clock module.",
    753: "The real time clock module is in emergency mode",
    754: "Information about the processors status.",
    755: "Information about the processors status.",
    757: "Real time clock module hardware error.",
    758: "Real time clock module is in emergency mode.",
    760: "Internal hardware fault.",
    761: "Information about the internal processors status.",
    762: "Information about the internal processors status.",
    763: "Information about the internal processors status.",
    764: "Information about the internal processors status.",
    765: "Information about the internal processors status.",
    766: "Emergency power derating has triggered.",
    767: "Information about the internal processors status.",
    768: "There is contrasting power limitation in the hardware modules",
    772: "Storage unit unavailable.",
    773: "Invalid country setup.",
    775: "The PMC power stage set unavailable.",
    776: "The device type is invalid.",
    779: "CAN bus transmission error.",
    781: "Information about the internal processors status.",
    782: "Information about the internal processors status.",
    783: "Information about the internal processors status.",
    784: "Information about the internal processors status.",
    785: "Information about the internal processors status.",
    786: "Information about the internal processors status.",
    787: "Information about the internal processors status.",
    788: "Information about the internal processors status.",
    789: "Information about the internal processors status.",
    790: "Information about the internal processors status.",
    791: "Information about the internal processors status.",
    792: "Information about the internal processors status.",
    793: "Information about the internal processors status.",
    794: "Information about the internal processors status.",
}
