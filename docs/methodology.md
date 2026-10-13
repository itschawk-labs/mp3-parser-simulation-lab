# Methodology

## Objective

The objective of this lab was to create a controlled, reproducible demonstration showing how untrusted metadata can influence application behavior when software intentionally reacts to a defined parsing condition.

The experiment was designed as a **simulation**, not as a real exploit.

---

## Test Artifacts

Two MP3 files were used:

### 1. Clean Control

`practice_audio.mp3`

This file acts as the control sample. It contains no `LAB_PARSER_TEST` field.

Expected behavior:

- MP3 plays normally
- test field is absent
- received test-field length is `0 bytes`
- no additional process is launched

### 2. Crafted Sample

`crafted_audio.mp3`

This file contains a custom ID3 `TXXX` field:

```text
LAB_PARSER_TEST
```

The test field contains approximately:

```text
2048 bytes
```

The toy player defines a simulated safe limit of:

```text
256 bytes
```

Expected behavior:

- MP3 begins playback
- custom test field is detected
- 2048-byte value exceeds the 256-byte simulated boundary
- application enters an intentionally programmed branch
- Calculator is launched as a benign demonstration action

---

## Application Logic

The toy player performs four relevant operations:

1. Opens the MP3 and reads ID3 metadata.
2. Searches for the custom `LAB_PARSER_TEST` field.
3. Measures the field length in bytes.
4. Compares the received length against the simulated 256-byte limit.

Conceptually:

```text
if field exists and field_size > simulated_limit:
    enter controlled demonstration branch
else:
    continue normal playback path
```

No memory corruption occurs.

---

## Clean Test Procedure

Run:

```powershell
python -u .\src\toy_player.py .\samples\practice_audio.mp3
```

Observed output:

```text
Test field present: False
Simulated safe limit: 256 bytes
Received: 0 bytes
Input accepted normally.
No trigger action.
```

---

## Crafted Test Procedure

Run:

```powershell
python -u .\src\toy_player.py .\samples\crafted_audio.mp3
```

Observed output:

```text
Test field present: True
Simulated safe limit: 256 bytes
Received: 2048 bytes
Simulated boundary violation detected.
Simulating control-flow compromise.
Benign demonstration action: launching Calculator.
```

---

## Hash Validation

SHA-256 values were generated for both files using PowerShell:

```powershell
Get-FileHash .\samples\practice_audio.mp3 -Algorithm SHA256
Get-FileHash .\samples\crafted_audio.mp3 -Algorithm SHA256
```

Recorded values:

```text
practice_audio.mp3
74F11969995207698A78C8284623C4A7C81FF87D1DCC5A578F75BF1232B03E62

crafted_audio.mp3
9B2FD8A85AE5205F836A60F2E6418D0DED7F11C5A795949CE402CAEE34F33D5D
```

The differing hashes confirm that the control and crafted samples are distinct file artifacts.

---

## Process-Monitor Validation

Microsoft Sysinternals Process Monitor was configured to focus on process creation associated with the Python process.

The relevant event showed:

```text
Process Name: python.exe
Operation:    Process Create
Path:         C:\WINDOWS\SYSTEM32\calc.exe
Result:       SUCCESS
```

The detailed event also recorded:

```text
PID:          33248
Command line: calc.exe
```

This validates that the toy application initiated the benign Calculator process.

---

## Evidence Preservation

The project preserves multiple evidence types:

- terminal execution logs
- SHA-256 hash record
- Procmon CSV export
- Procmon native PML capture
- annotated/redacted presentation screenshots

Presentation screenshots are not treated as raw evidence. Raw logs and Procmon captures are retained separately.

---

## Interpretation

The test does **not** demonstrate that an MP3 file independently executes code.

It demonstrates that:

1. an application can parse untrusted media metadata,
2. application logic can react to that parsed input,
3. a controlled branch can launch another process,
4. the resulting process behavior can be validated through forensic tooling.
