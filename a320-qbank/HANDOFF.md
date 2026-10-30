# Paquete de transferencia — Banco DGAC A320

Banco de preguntas de la DGAC Chile para la habilitación de tipo **Airbus A320** (enero 2018): 621 preguntas en 11 grupos de sistemas, cada una con su respuesta, una explicación en español, la referencia al FCOM y un nivel de confianza. Incluye una página interactiva lista para usar.

## Contenido

| Ruta | Qué es |
|---|---|
| `data/a320_dgac_qbank.json` | **Fuente de verdad.** Banco completo con respuestas (esquema abajo). |
| `data/questions_raw.json` | Preguntas tal como se extrajeron del PDF, sin respuestas (para auditoría). |
| `src/app.template.html` | Página interactiva (HTML + CSS + JS vanilla, sin dependencias). Los datos se inyectan en `/*__DATA__*/null`. |
| `tools/build.py` | Genera `dist/` a partir de la plantilla y el JSON. |
| `dist/a320-qbank.html` | Página autónoma con los datos embebidos. Se abre con doble clic, sin servidor. |
| `dist/artifact.html` | La misma página como fragmento para publicar como Artifact de claude.ai. |

Después de editar el JSON o la plantilla: `python3 tools/build.py`.

## Esquema JSON (`a320-dgac-qbank/v1`)

```jsonc
{
  "schema": "a320-dgac-qbank/v1",
  "source": "...", "generated": "2026-10-30",
  "confidenceLegend": { "h": "...", "m": "...", "l": "..." },
  "groups": [{
    "id": "aircond",                       // slug estable, se usa en la URL (#aircond)
    "name": "AIR COND. & PNEUMATICS",      // nombre original de la DGAC
    "nameEs": "Aire acondicionado y neumático",
    "questions": [{
      "id": "aircond-1",                   // único: <grupo>-<n>
      "n": 1,                              // número en el PDF de la DGAC
      "q": "AFT CARGO INDICATIONS ...",    // enunciado original (inglés)
      "options": [{ "key": "A", "text": "..." }],
      "answer": "D",                       // clave correcta
      "confidence": "h",                   // h alta · m verificar · l dudosa
      "explanation": "...",                // justificación en español
      "fcomRef": "DSC-21-30"               // capítulo del FCOM donde verificar
    }]
  }]
}
```

Grupos: Aire acondicionado y neumático (85), Vuelo automático y FMS (83), Comunicaciones y oxígeno (51), Sistema eléctrico (75), Protección contra incendio (33), Combustible e hidráulico (49), Indicación y registro (15), APU y plantas de poder (52), Controles de vuelo (67), Protección hielo y lluvia (30), Tren, luces y puertas (81).

## Cómo integrarlo en otro proyecto

- **React / cualquier framework:** importar `data/a320_dgac_qbank.json` y renderizar `groups[].questions[]`. La lógica de la plantilla (corrección inmediata, filtros Todas / Sin responder / Falladas / Para verificar, mezclar, teclado A–F y ← →, progreso en `localStorage` con la clave `a320-dgac-qbank:v1`) es fácil de portar a componentes.
- **Embebido tal cual:** servir `dist/a320-qbank.html` o meterlo en un `<iframe>`.
- **Otra sesión de Claude:** pasarle este README y el JSON. Con eso alcanza para reconstruir o extender la app.

## Estado de la verificación con el FCOM

En esta sesión **no hubo una copia del FCOM disponible**. No se encontró una sesión "Aero Study Platform" ni un FCOM en Google Drive. Las respuestas salen del conocimiento del FCOM A320 (ceo, capítulos DSC/LIM) y quedaron clasificadas así:

- **h (alta):** 543 preguntas. Coinciden con el FCOM tal como lo conozco.
- **m (verificar):** 74 preguntas. La respuesta es probable, pero depende de la revisión del FCOM, del motor (CFM/IAE) o de una redacción ambigua de la DGAC.
- **l (dudosa):** 4 preguntas. Faltan datos firmes para confirmarlas.

**Tarea pendiente para la sesión que tenga el FCOM:** revisar la tabla de abajo. Para cada pregunta, confirmar o corregir `answer`, ajustar `explanation` y `fcomRef`, y cambiar `confidence` a `"h"`. Después, ejecutar `python3 tools/build.py`.

### Preguntas para verificar (78)

| id | Grupo | Nº | Resp. | Confianza | FCOM | Enunciado |
|---|---|---|---|---|---|---|
| `aircond-2` | Aire acondicionado y neumático | 2 | **B** | media | DSC-21-30 | AFT CARGO VENTILATION IS CONTROLLED BY: |
| `aircond-3` | Aire acondicionado y neumático | 3 | **B** | media | DSC-21-20 | AN AMBER FAULT LIGHT IN THE HOT AIR P/B INDICATES: |
| `aircond-9` | Aire acondicionado y neumático | 9 | **A** | media | DSC-21-40 | BOTH PRESSURIZATION AUTO CONTROLLERS ARE SET BY THE ACTIVE FLIGHT PLAN LOADED IN THE MCDU.… |
| `aircond-16` | Aire acondicionado y neumático | 16 | **C** | media | DSC-21-20 | HOT AIR PRESS. REG. VALVE FAILED OPEN. |
| `aircond-19` | Aire acondicionado y neumático | 19 | **B** | media | DSC-21-40 | HOW MANY OUTFLOW VALVES ARE THERE? |
| `aircond-24` | Aire acondicionado y neumático | 24 | **C** | media | DSC-21-40 | IF YOU SELECT A POSITION OTHER THAN THE AUTO DETENT ON THE LDG ELEV AUTO SELECTOR, HOW CAN… |
| `aircond-25` | Aire acondicionado y neumático | 25 | **A** | media | DSC-36-10 | IN FLIGHT IF THE AIR PRESSURE IS INSUFFICIENT EVEN WITH THE HP VALVE OPEN: |
| `aircond-32` | Aire acondicionado y neumático | 32 | **D** | media | DSC-21-50 | PLACING THE AVIONICS VENTILATION SYSTEM IN THE SMOKE CONFIGURATION: |
| `aircond-33` | Aire acondicionado y neumático | 33 | **C** | media | DSC-21-50 | PLACING THE BLOWER PUSH BUTTON TO OVERRIDE: |
| `aircond-34` | Aire acondicionado y neumático | 34 | **C** | media | DSC-21-50 | PLACING THE EXTRACT PUSH BUTTON TO OVERRIDE: |
| `aircond-42` | Aire acondicionado y neumático | 42 | **B** | media | DSC-21-20 | THE HOT AIR VALVE PUSH BUTTON CONTROLS: |
| `aircond-51` | Aire acondicionado y neumático | 51 | **A** | media | DSC-21-30 | THE VENT FAN RUNS ANY TIME THERE IS A NORMAL SHIPS POWER AND THE ISOLATION VALVES ARE OPEN… |
| `aircond-62` | Aire acondicionado y neumático | 62 | **C** | media | DSC-21-20 | WHAT IS THE FUNCTION OF THE PACK FLOW SELECTOR? |
| `aircond-71` | Aire acondicionado y neumático | 71 | **D** | media | DSC-21-40 | WHEN DOES NORMAL DEPRESSURIZATION OCCUR? |
| `autoflight-3` | Vuelo automático y FMS | 3 | **A** | media | DSC-31-40 | ALL PFD DISPLAYS EXCEPT ATTITUDE; SPEED; HEADING; ALTITUDE; AND VERTICAL SPEED ARE REMOVED… |
| `autoflight-13` | Vuelo automático y FMS | 13 | **C** | media | DSC-22_20 | DASHES ON THE MCDU INDICATE DATA: |
| `autoflight-16` | Vuelo automático y FMS | 16 | **C** | media | DSC-22_20 | FMGC 1 IS NOT WORKING. TO ENTER DATA INTO THE FMGC, WHICH MCDU WOULD YOU USE? |
| `autoflight-19` | Vuelo automático y FMS | 19 | **D** | media | DSC-22_20 | HOW DOES THE FMGC COMPUTE RADIO POSITION? |
| `autoflight-24` | Vuelo automático y FMS | 24 | **B** | media | DSC-22_30 | IF YOU HAVE DEPRESSED THE EXPED PUSH BUTTON AND WANT TO CANCEL THIS FUNCTION, HOW COULD TH… |
| `autoflight-25` | Vuelo automático y FMS | 25 | **C** | media | DSC-31-40 | ILS 1 INFORMATION IS DISPLAYED ON _______ WHEN OPERATING IN THE ROSE ILS MODE: |
| `autoflight-30` | Vuelo automático y FMS | 30 | **B** | media | DSC-22_30 | ONE A/P CAN BE ENGAGED ON THE GROUND IF THE ENGINES ARE NOT RUNNING. |
| `autoflight-38` | Vuelo automático y FMS | 38 | **C** | media | DSC-22_30 | THE CAPTAIN\'S FMA INDICATES - FD2 IN COLUMN FIVE, LINE TWO. WHAT DOES THIS MEAN? |
| `autoflight-40` | Vuelo automático y FMS | 40 | **A** | media | DSC-31-40 | THE ENERGY CIRCLE IS A GREEN ARC, CENTERED ON THE AIRCRAFT'S POSITION AND ORIENTED TOWARDS… |
| `autoflight-49` | Vuelo automático y FMS | 49 | **D** | media | DSC-22_10 | THE PILOT INTERFACES WITH THE FMGS USING THE: |
| `autoflight-53` | Vuelo automático y FMS | 53 | **A** | media | DSC-34 | THE STANDBY ATTITUDE INDICATION WILL REMAIN AVAILABLE FOR _____ MINUTES AFTER TOTAL ELECTR… |
| `autoflight-77` | Vuelo automático y FMS | 77 | **B** | media | DSC-22_20 | WHILE TAXIING ON THE GROUND, THE FMGS DISPLAYS THE POSTITION OF THE AIRCRAFT USING: |
| `autoflight-81` | Vuelo automático y FMS | 81 | **B** | media | DSC-22_30 | YOU CAN DISENGAGE THE EXPEDITE MODE BY: |
| `comms-1` | Comunicaciones y oxígeno | 1 | **A** | media | DSC-35 | APPROXIMATELY HOW LONG ARE THE PASSENGER OXYGEN GENERATORS ABLE TO PRODUCE OXYGEN? |
| `comms-9` | Comunicaciones y oxígeno | 9 | **C** | media | DSC-23 | IF RMP NAVIGATION TUNING IS CURRENTLY IN USE FOR VOR TUNING AND ATC ASSIGNS A NEW COMMUNIC… |
| `comms-10` | Comunicaciones y oxígeno | 10 | **B** | media | DSC-23 | IF THE VHF 3 TRANSMISSION KEY ILUMINATED AMBER SHOWING THE WORD CALL: |
| `comms-11` | Comunicaciones y oxígeno | 11 | **A** | media | DSC-23 | IF YOU DEPRESS THE GUARDED NAV BUTTON, THE MCDU RAD NAV PAGES ARE INHIBITED AND THE RMP CO… |
| `comms-16` | Comunicaciones y oxígeno | 16 | **B** | media | DSC-31 | ONLY THE LAST 60 MINUTES OF RECORDING ARE RETAINED BY THE CVR. |
| `comms-21` | Comunicaciones y oxígeno | 21 | **C** | media | DSC-23 | RMP #1 IS DEDICATED TO WHICH VHF RADIOS |
| `comms-29` | Comunicaciones y oxígeno | 29 | **A** | media | DSC-35 | THERE ARE OXYGEN GENERATORS IN EACH AIRCRAFT'S GALLEY. |
| `comms-30` | Comunicaciones y oxígeno | 30 | **A** | baja | DSC-23 | THERE ARE TWO SERVICE INTERPHONE JACKS IN THE HYDRAULIC COMPARTMENT. |
| `comms-31` | Comunicaciones y oxígeno | 31 | **B** | baja | DSC-23 | THE SERVICE INTERPHONE HAS _____ INTERPHONE JACKS AND AN OVRD SWITCH LOCATED ON THE OVERHE… |
| `comms-42` | Comunicaciones y oxígeno | 42 | **A** | media | DSC-23 | WHEN LOOKING AT EITHER RMP, HOW IS IT POSSIBLE TO DETERMINE IF AN RMP IS SELECTED TO A VHR… |
| `comms-43` | Comunicaciones y oxígeno | 43 | **A** | media | DSC-23 | WHEN RMP1 (RADIO MANAGEMENT PANEL) OR RMP2 IS OFF, RPM3 IS STILL ABLE TO CONTROL VHF/HF TR… |
| `comms-47` | Comunicaciones y oxígeno | 47 | **C** | media | DSC-23 | WHICH ACP SWITCH CONFIGURATION IS CORRECT FOR COMMUNICATION WITH OTHER COCKPIT CREW MEMBER… |
| `comms-51` | Comunicaciones y oxígeno | 51 | **B** | media | DSC-22_20 | YOU CAN TUNE THE ILS RECEIVERS TO DIFFERENT CHANNELS |
| `elec-14` | Sistema eléctrico | 14 | **C** | media | DSC-24 | FOR THE A-320 THE EMERGENCY GENERATOR SUPPLIES POWER AS LOGN AS RAT IS DEPLOYED AND: |
| `elec-24` | Sistema eléctrico | 24 | **D** | media | DSC-33 | IF NORMAL ELECTRICAL POWER IS LOST; ESSENTIAL COCKPIT LIGHTING IS MAINTANIRED FOR THE: |
| `elec-33` | Sistema eléctrico | 33 | **A** | media | DSC-24 | THE AC ESSENTIAL BUS IS POWERED BY THE BATTERY AT SPEED ABOVE 50 KT. |
| `elec-45` | Sistema eléctrico | 45 | **B** | media | DSC-33 | WHAT COCKPIT LIGHTING IS AVAILABLE DURING AN EMERGENCY ELECTRICAL SITUATION? |
| `elec-67` | Sistema eléctrico | 67 | **A** | media | DSC-24 | WHICH RADIOS ARE INOPERATIVE WITH GEAR EXTENSION WHILE IN THE EMERGENCY ELECTRICAL CONFIGU… |
| `elec-68` | Sistema eléctrico | 68 | **C** | media | PRO-NOR | WHICH VOLTAGE REQUIRES RECHARGING OR REPLACING THE BATTERIES? |
| `elec-75` | Sistema eléctrico | 75 | **D** | media | PRO-NOR | YOU ENTER A DARK COCKPIT, WHAT ACTION IS NECESSARY BEFORE CHECKING THE BATTERY VOLTAGES? |
| `fire-17` | Protección contra incendio | 17 | **B** | media | DSC-26 | IF YOU PERFORM THE APU FIRE TEST WITH ONLY DC POWER AVAILABLE, YOU GET THE MASTER WARN ON … |
| `fire-24` | Protección contra incendio | 24 | **B** | media | DSC-26 | THE AFT CARGO COMPARTMENT SMOKE DETECTION SYSTEM CONSISTS OF: |
| `fire-26` | Protección contra incendio | 26 | **A** | media | DSC-26 | THE AVIONICS COMPARTMENT IS THE ONLY AREA WHERE THERE IS NO FIRE EXTINGUISHING SYSTEM INST… |
| `fire-33` | Protección contra incendio | 33 | **C** | media | DSC-26 | WITH REFERENCE TO CARGO COMPARTMENT FIRE EXTINGUISHING, WHICH STATEMENT IS TRUE? |
| `fuelhyd-7` | Combustible e hidráulico | 7 | **C** | media | DSC-28 | CAN THE POSITION OF THE WING FUEL TRANSFER VALVES BE CHECKED? |
| `fuelhyd-8` | Combustible e hidráulico | 8 | **C** | media | DSC-28 | CENTER TANK PUMPS DO NOT STOP 5 MIN AFTER CENTER TANK LOW LEVEL REACHED. WHERE WE CAN SEE … |
| `fuelhyd-18` | Combustible e hidráulico | 18 | **B** | media | DSC-29 | HOW MANY PUMPS HAVE THE YELLOW SYSTEM TO PROVIDE PRESSURE (NOT COUNTING THE PTU)? |
| `fuelhyd-19` | Combustible e hidráulico | 19 | **B** | media | DSC-29 | IT IS POSSIBLE TO PRESSURIZE THE GREEN HYDRAULIC SYSTEM ON THE GROUND VIA THE PTU WHEN THE… |
| `fuelhyd-23` | Combustible e hidráulico | 23 | **C** | media | DSC-29 | THE ENG PUMP FAULT LIGHT EXTINGUISHES WHEN THE ENGINE PUMP SWITCH IS SELECTED TO OFF EXCEP… |
| `fuelhyd-49` | Combustible e hidráulico | 49 | **D** | media | DSC-28 | WITH THE CENTER TANK PUMP MODE SEL SWITCH IN AUTO; THE CENTER TANK PUMPS: |
| `indicating-2` | Indicación y registro | 2 | **A** | media | DSC-31 | AN "STS" MESSAGE WILL FLASH ON THE ENGINE/WARNING DISPLAY AFTER ENGINE SHUTDOWN TO: |
| `apu-2` | APU y plantas de poder | 2 | **C** | media | DSC-24 | BAT 1 AND 2 PUSH BUTTONS DO NOT NEED TO BE SELECTED ON IF EXTERNAL POWER IS AVAILABLE. |
| `apu-5` | APU y plantas de poder | 5 | **D** | media | DSC-70 | DURING AN AUTOMATIC START SEQUENCE, SELECTING THE ENG MASTER SWITCH TO ON: |
| `apu-6` | APU y plantas de poder | 6 | **B** | media | DSC-49 | FIRE ON GROUND OR IN FLIGHT WILL CAUSE THE APU MASTER SW PUSHBUTTON FAULT LIGHT TO COME ON… |
| `apu-7` | APU y plantas de poder | 7 | **B** | media | DSC-49 | FIRE ON GROUND OR IN FLIGHT WILL CAUSE THE APU MASTER SW PUSHBUTTON FAULT LIGHT TO COME ON… |
| `apu-10` | APU y plantas de poder | 10 | **C** | media | LIM-49 | MAXIMUM ALTITUDE FOR APU BLEED OPERATION IS: |
| `apu-11` | APU y plantas de poder | 11 | **D** | media | DSC-49 | ON GROUND, THE NO BREAK POWER TRANSFER FUNCTION IS INHIBITED IN CASE OF APU SHUTDOWN GENER… |
| `apu-12` | APU y plantas de poder | 12 | **A** | baja | DSC-49 | THE APU BLEED VALVE IS AUTOMATICALLY CLOSED ABOVE ____ FEET DESCENDING BY THE ECB. |
| `apu-17` | APU y plantas de poder | 17 | **D** | media | LIM-49 | THE APU MAY BE STARTED UP TO WHAT ALTITUDE? |
| `apu-31` | APU y plantas de poder | 31 | **B** | media | DSC-70 | THE NORMAL MODE TO SET THRUST IS: |
| `fctl-35` | Controles de vuelo | 35 | **A** | media | DSC-27 | THE MESSAGE WING TIP BRK ON APPEARS ON THE E/WD. WHAT DOES IT MEAN? |
| `fctl-36` | Controles de vuelo | 36 | **A** | media | DSC-27 | THE SPOILER PANELS ARE THE ONLY FLIGHT CONTROL SURFACES WITH NO REDUNDANT CONTROL. |
| `fctl-50` | Controles de vuelo | 50 | **C** | media | DSC-27 | WHAT HAPPENS TO THE RUDDER LIMITS IF BOTH FAC'S FAULT? |
| `gear-3` | Tren, luces y puertas | 3 | **A** | media | DSC-32 | AUTO BRAKE MAY BE ARMED WITH THE PARKING BRAKE ON. |
| `gear-8` | Tren, luces y puertas | 8 | **B** | media | DSC-32 | CAN THE GEAR BE EXTENDED ABOVE 260 KTS IF NECESSARY? |
| `gear-23` | Tren, luces y puertas | 23 | **B** | media | DSC-32 | IF THE BSCU DETECTS A BRAKE SYSTEM MALFUNCTION IN FLIGHT WITH THE A/SKID & N/W STRG SWITCH… |
| `gear-38` | Tren, luces y puertas | 38 | **C** | media | DSC-52 | THE COCKPIT DOOR: |
| `gear-55` | Tren, luces y puertas | 55 | **A** | media | DSC-35 | WHAT ARE THE INDICATIONS THAT THE PBE OXYGEN SUPPLY HAS DEPLETED? |
| `gear-56` | Tren, luces y puertas | 56 | **D** | media | DSC-33 | WHAT COCKPIT LIGHTING IS AVAILABLE DURING AN EMERGENCY ELECTRICAL CONFIGURATION (EEC)? |
| `gear-63` | Tren, luces y puertas | 63 | **A** | baja | LIM-35 | WHAT IS CREW OXYGEN MINUMUM PRESSURE, WHERE CAN IT BE READ? |
| `gear-70` | Tren, luces y puertas | 70 | **A** | media | DSC-29 | WHEN THE ELECTRIC PUMP IS OPERATING THE FWD OR AFT CARGO DOORS, THE ONLY OTHER YELLOW SYST… |
