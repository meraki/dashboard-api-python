# Generation Report

## 2026-05-14 | Library v3.1.0b1 | API 1.70.0-beta.1


### Python keyword parameter conflicts


The following operations have parameters whose names are Python reserved keywords.
The generator renames them with a trailing underscore (e.g., `from` -> `from_`).
These should be reported to the owning teams for resolution in the API spec.


| Scope | Operation | Location | Param |
| --- | --- | --- | --- |
| secureConnect | `createOrganizationSecureConnectRemoteAccessLogsExport` | body | `from` |

## 2026-05-06 | Library v3.1.0b0 | API 1.70.0-beta.0


### Python keyword parameter conflicts


The following operations have parameters whose names are Python reserved keywords.
The generator renames them with a trailing underscore (e.g., `from` -> `from_`).
These should be reported to the owning teams for resolution in the API spec.


| Scope | Operation | Location | Param |
| --- | --- | --- | --- |
| secureConnect | `createOrganizationSecureConnectRemoteAccessLogsExport` | body | `from` |

