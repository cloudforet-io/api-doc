---
description: null
---

# Secret Group

> **Package : spaceone.api.secret.v1**

## SecretGroup

{% hint style="info" %}
**SecretGroup Methods:**
{% endhint %}

| NO | Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [create](secret-group.md#create) | [CreateSecretGroupRequest](secret-group.md#createsecretgrouprequest) | [SecretGroupInfo](secret-group.md#secretgroupinfo) |  |
| 2 | [update](secret-group.md#update) | [UpdateSecretGroupRequest](secret-group.md#updatesecretgrouprequest) | [SecretGroupInfo](secret-group.md#secretgroupinfo) |  |
| 3 | [add\_secret](secret-group.md#add_secret) | [SecretGroupSecretRequest](secret-group.md#secretgroupsecretrequest) | [SecretGroupSecretInfo](secret-group.md#secretgroupsecretinfo) |  |
| 4 | [remove\_secret](secret-group.md#remove_secret) | [SecretGroupSecretRequest](secret-group.md#secretgroupsecretrequest) | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |  |
| 5 | [delete](secret-group.md#delete) | [SecretGroupRequest](secret-group.md#secretgrouprequest) | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |  |
| 6 | [get](secret-group.md#get) | [GetSecretGroupRequest](secret-group.md#getsecretgrouprequest) | [SecretGroupInfo](secret-group.md#secretgroupinfo) |  |
| 7 | [list](secret-group.md#list) | [SecretGroupQuery](secret-group.md#secretgroupquery) | [SecretGroupsInfo](secret-group.md#secretgroupsinfo) |  |
| 8 | [stat](secret-group.md#stat) | [SecretGroupStatQuery](secret-group.md#secretgroupstatquery) | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  |

### create

> **POST** /secret/v1/secret-groups

| Type | Message |
| :--- | :--- |
| Request | [CreateSecretGroupRequest](secret-group.md#createsecretgrouprequest) |
| Response | [SecretGroupInfo](secret-group.md#secretgroupinfo) |

### update

> **PUT** /secret/v1/secret-group/{secret\_group\_id}

| Type | Message |
| :--- | :--- |
| Request | [UpdateSecretGroupRequest](secret-group.md#updatesecretgrouprequest) |
| Response | [SecretGroupInfo](secret-group.md#secretgroupinfo) |

### add\_secret

> **POST** /secret/v1/secret-group/{secret\_group\_id}/secrets

| Type | Message |
| :--- | :--- |
| Request | [SecretGroupSecretRequest](secret-group.md#secretgroupsecretrequest) |
| Response | [SecretGroupSecretInfo](secret-group.md#secretgroupsecretinfo) |

### remove\_secret

> **DELETE** /secret/v1/secret-group/{secret\_group\_id}/secret/{secret\_id}

| Type | Message |
| :--- | :--- |
| Request | [SecretGroupSecretRequest](secret-group.md#secretgroupsecretrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |

### delete

> **DELETE** /secret/v1/secret-group/{secret\_group\_id}

| Type | Message |
| :--- | :--- |
| Request | [SecretGroupRequest](secret-group.md#secretgrouprequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |

### get

> **GET** /secret/v1/secret-group/{secret\_group\_id}

| Type | Message |
| :--- | :--- |
| Request | [GetSecretGroupRequest](secret-group.md#getsecretgrouprequest) |
| Response | [SecretGroupInfo](secret-group.md#secretgroupinfo) |

### list

> **GET** /secret/v1/secret-groups
>
> **POST** /secret/v1/secret-groups/search

| Type | Message |
| :--- | :--- |
| Request | [SecretGroupQuery](secret-group.md#secretgroupquery) |
| Response | [SecretGroupsInfo](secret-group.md#secretgroupsinfo) |

### stat

> **POST** /secret/v1/secret-groups/stat

| Type | Message |
| :--- | :--- |
| Request | [SecretGroupStatQuery](secret-group.md#secretgroupstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |

## Message

### CreateSecretGroupRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name | string | ✅ |  |
| 2 | tags | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ❌ |  |
| 3 | domain\_id | string | ✅ |  |

### GetSecretGroupRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | secret\_group\_id | string | ✅ |  |
| 2 | domain\_id | string | ✅ |  |
| 3 | only | string | ❌ |  |

### SecretGroupInfo

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | secret\_group\_id | string |  |  |
| 2 | name | string |  |  |
| 3 | tags | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |  |  |
| 4 | domain\_id | string |  |  |
| 5 | created\_at | [google.protobuf.Timestamp](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto) |  |  |

### SecretGroupQuery

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query | [spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query) | ❌ |  |
| 2 | secret\_group\_id | string | ❌ |  |
| 3 | name | string | ❌ |  |
| 4 | secret\_id | string | ❌ |  |
| 5 | domain\_id | string | ✅ |  |

### SecretGroupRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | secret\_group\_id | string | ✅ |  |
| 2 | domain\_id | string | ✅ |  |

### SecretGroupSecretInfo

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | secret\_group\_info | [SecretGroupInfo](secret-group.md#secretgroupinfo) |  |  |
| 2 | secret\_info | [SecretInfo](secret-group.md#secretinfo) |  |  |
| 3 | domain\_id | string |  |  |

### SecretGroupSecretRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | secret\_group\_id | string | ✅ |  |
| 2 | secret\_id | string | ✅ |  |
| 3 | domain\_id | string | ✅ |  |

### SecretGroupStatQuery

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query | [spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query) | ✅ |  |
| 2 | domain\_id | string | ✅ |  |

### SecretGroupsInfo

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | results | [SecretGroupInfo](secret-group.md#secretgroupinfo) |  |  |
| 2 | total\_count | [int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) |  |  |

### UpdateSecretGroupRequest

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | secret\_group\_id | string | ✅ |  |
| 2 | name | string | ❌ |  |
| 3 | tags | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ❌ |  |
| 4 | domain\_id | string | ✅ |  |

