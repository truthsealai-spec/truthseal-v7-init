# Judicial Veto Lane (JVL) v1.0
Non-bypassable hardware kill switch – the physical embodiment of ULLI

Goal
Even if the AI, OS, firmware, or hypervisor is compromised, a single hardware signal can stop the action at the last nanosecond.

Design
- One dedicated, physically isolated signal path from the AEGIS core to the commitment gate/actuator
- Hard-wired logic – no software can delay, re-map, or override
- Triggered by TDC failure or external sovereign kill command
- Already exists today in safety PLCs (SIL-4 / ASIL-D) and NVIDIA Safety Island

This is the line that protects life when everything else fails.
