# Limitations and Scope

## This Is Not a Real Exploit

This project intentionally simulates a parser-boundary condition.

It does **not** demonstrate:

- a real buffer overflow
- a heap overflow
- a stack overflow
- use-after-free
- arbitrary memory corruption
- shellcode execution
- return-oriented programming
- privilege escalation
- persistence
- credential theft
- command-and-control activity
- a VLC vulnerability
- a Windows Media Player vulnerability
- an MP3-format vulnerability

---

## Controlled Application Logic

The toy player deliberately checks whether a custom ID3 field exceeds a defined threshold.

The resulting Calculator launch occurs because the application was intentionally programmed to do so.

Therefore, the accurate description is:

> **controlled media-parser simulation**

or:

> **simulated media-file-triggered execution chain**

It should not be described as:

> “an MP3 that executes code by itself”

or:

> “a real MP3 exploit”

---

## Evidence Limitations

The public PNG screenshots are presentation-edited copies.

They may contain:

- cropping
- visual highlighting
- privacy redaction

They are intended to improve readability and should not be treated as primary raw forensic evidence.

The raw evidence is preserved through:

- terminal text logs
- SHA-256 values
- Procmon CSV
- Procmon PML

---

## Platform Scope

This lab was performed on Windows and uses Windows Calculator as the benign demonstration action.

Behavior may differ across:

- operating systems
- Python versions
- audio backends
- ID3 libraries
- Windows Calculator implementations

---

## Security Scope

The project was intentionally designed to avoid weaponization.

Its purpose is to demonstrate:

- input handling
- parser-boundary concepts
- control-flow reasoning
- process validation
- forensic evidence collection
- technical communication
