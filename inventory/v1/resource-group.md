---
description: A ResourceGroup is a group of `resource`s from various `provider`s.
---
# Resource group

>  **Package : spaceone.api.inventory.v1**

## ResourceGroup

{% hint style="info" %}
**ResourceGroup Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](resource-group.md#create)|   [CreateResourceGroupRequest](resource-group.md#createresourcegrouprequest) |   [ResourceGroupInfo](resource-group.md#resourcegroupinfo) |
| [**update**](resource-group.md#update)|   [UpdateResourceGroupRequest](resource-group.md#updateresourcegrouprequest) |   [ResourceGroupInfo](resource-group.md#resourcegroupinfo) |
| [**delete**](resource-group.md#delete)|   [ResourceGroupRequest](resource-group.md#resourcegrouprequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**get**](resource-group.md#get)|   [GetResourceGroupRequest](resource-group.md#getresourcegrouprequest) |   [ResourceGroupInfo](resource-group.md#resourcegroupinfo) |
| [**list**](resource-group.md#list)|   [ResourceGroupQuery](resource-group.md#resourcegroupquery) |   [ResourceGroupsInfo](resource-group.md#resourcegroupsinfo) |
| [**stat**](resource-group.md#stat)|   [ResourceGroupStatQuery](resource-group.md#resourcegroupstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
### create
> **POST** /inventory/v1/resource-group/create
>

> Creates a new ResourceGroup. You can integrate `resource`s from different `provider`s by specifying the cloud resources to be grouped in the `resources` parameter.

| Type | Message |
| :--- | :--- |
| Request | [CreateResourceGroupRequest](resource-group.md#createresourcegrouprequest) |
| Response |  [ResourceGroupInfo](resource-group.md#resourcegroupinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "name": "azure-group-1",
    "resources": [
        {
            "resource_type": "inventory.Server?provider=azure&cloud_service_group=Compute&cloud_service_type=VirtualMachine",
            "filter": [
                {
                    "o": "eq",
                    "k": "provider",
                    "v": "azure"
                },
                {
                    "o": "eq",
                    "k": "cloud_service_group",
                    "v": "Compute"
                },
                {
                    "o": "eq",
                    "k": "cloud_service_type",
                    "v": "VirtualMachine"
                }
            ]
        }
    ],
    "options": {
        "raw_filter": []
    },
    "tags": {
        "a": "b"
    }
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "resource_group_id": "rsc-grp-7d46a1fc7738",
    "name": "azure-group-1",
    "resources": [
        {
            "resource_type": "inventory.Server?provider=azure&cloud_service_group=Compute&cloud_service_type=VirtualMachine",
            "filter": [
                {
                    "k": "provider",
                    "v": "azure",
                    "o": "eq"
                },
                {
                    "k": "cloud_service_group",
                    "v": "Compute",
                    "o": "eq"
                },
                {
                    "k": "cloud_service_type",
                    "v": "VirtualMachine",
                    "o": "eq"
                }
            ]
        }
    ],
    "options": {
        "raw_filter": []
    },
    "tags": {
        "a": "b"
    },
    "domain_id": "domain-58010aa2e451",
    "created_at": "2022-06-23T01:50:33.152Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### update
> **POST** /inventory/v1/resource-group/update
>

> Updates a specific ResourceGroup. You can make changes in ResourceGroup settings, including `name`, `tags`, and grouped resources in the ResourceGroup.

| Type | Message |
| :--- | :--- |
| Request | [UpdateResourceGroupRequest](resource-group.md#updateresourcegrouprequest) |
| Response |  [ResourceGroupInfo](resource-group.md#resourcegroupinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "resource_group_id": "rsc-grp-7d46a1fc7738",
    "name": "azure-grp-test2",
    "resources": [
        {
            "resource_type": "inventory.Server?provider=azure&cloud_service_group=Compute&cloud_service_type=VirtualMachine",
            "filter": [
                {
                    "k": "provider",
                    "v": "azure",
                    "o": "eq"
                },
                {
                    "o": "eq",
                    "k": "cloud_service_group",
                    "v": "Compute"
                },
                {
                    "v": "VirtualMachine",
                    "k": "cloud_service_type",
                    "o": "eq"
                }
            ]
        }
    ],
    "options": {},
    "tags": {
        "b": "c"
    }
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "resource_group_id": "rsc-grp-7d46a1fc7738",
    "name": "azure-grp-test2",
    "resources": [
        {
            "resource_type": "inventory.Server?provider=azure&cloud_service_group=Compute&cloud_service_type=VirtualMachine",
            "filter": [
                {
                    "k": "provider",
                    "v": "azure",
                    "o": "eq"
                },
                {
                    "k": "cloud_service_group",
                    "v": "Compute",
                    "o": "eq"
                },
                {
                    "k": "cloud_service_type",
                    "v": "VirtualMachine",
                    "o": "eq"
                }
            ]
        }
    ],
    "options": {
        "raw_filter": []
    },
    "tags": {
        "a": "b"
    },
    "domain_id": "domain-58010aa2e451",
    "created_at": "2022-06-23T01:50:33.152Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### delete
> **POST** /inventory/v1/resource-group/delete
>

> Deletes a specific ResourceGroup. You must specify the `resource_group_id` of the ResourceGroup to delete.

| Type | Message |
| :--- | :--- |
| Request | [ResourceGroupRequest](resource-group.md#resourcegrouprequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "resource_group_id": "rsc-grp-aa3c4ca465b2"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### get
> **POST** /inventory/v1/resource-group/get
>

> Gets a specific ResourceGroup. Prints detailed information about the ResourceGroup, including the information of the grouped cloud resources.

| Type | Message |
| :--- | :--- |
| Request | [GetResourceGroupRequest](resource-group.md#getresourcegrouprequest) |
| Response |  [ResourceGroupInfo](resource-group.md#resourcegroupinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "resource_group_id": "rsc-grp-aa3c4ca465b2"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "resource_group_id": "rsc-grp-aa3c4ca465b2",
    "name": "stset",
    "resources": [
        {
            "resource_type": "inventory.Server?provider=aws&cloud_service_group=EC2&cloud_service_type=Instance",
            "filter": [
                {
                    "k": "provider",
                    "o": "eq",
                    "v": "aws"
                },
                {
                    "v": "EC2",
                    "k": "cloud_service_group",
                    "o": "eq"
                },
                {
                    "o": "eq",
                    "k": "cloud_service_type",
                    "v": "Instance"
                }
            ],
            "keyword": "test"
        }
    ],
    "options": {
        "raw_filter": []
    },
    "tags": {},
    "project_id": "project-18655561c535",
    "domain_id": "domain-58010aa2e451",
    "created_at": "2021-06-01T10:23:20.537Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### list
> **POST** /inventory/v1/resource-group/list
>

> Gets a list of all ResourceGroups. You can use a query to get a filtered list of ResourceGroups.

| Type | Message |
| :--- | :--- |
| Request | [ResourceGroupQuery](resource-group.md#resourcegroupquery) |
| Response |  [ResourceGroupsInfo](resource-group.md#resourcegroupsinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "query": {
        "filter": [
            {
                "key": "name",
                "value": [
                    "azure-vmss-group",
                    "stset"
                ],
                "operator": "in"
            }
        ]
    }
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "results": [
        {
            "resource_group_id": "rsc-grp-4c86e071e0f0",
            "name": "azure-vmss-group",
            "resources": [
                {
                    "resource_type": "inventory.CloudService?provider=azure&cloud_service_group=Compute&cloud_service_type=VmScaleSet",
                    "filter": [
                        {
                            "k": "provider",
                            "v": "azure",
                            "o": "eq"
                        },
                        {
                            "v": "Compute",
                            "k": "cloud_service_group",
                            "o": "eq"
                        },
                        {
                            "k": "cloud_service_type",
                            "v": "VmScaleSet",
                            "o": "eq"
                        }
                    ]
                }
            ],
            "options": {
                "raw_filter": []
            },
            "tags": {},
            "project_id": "project-9074eea97d7e",
            "domain_id": "domain-58010aa2e451",
            "created_at": "2021-04-23T03:23:40.037Z"
        },
        {
            "resource_group_id": "rsc-grp-aa3c4ca465b2",
            "name": "stset",
            "resources": [
                {
                    "resource_type": "inventory.Server?provider=aws&cloud_service_group=EC2&cloud_service_type=Instance",
                    "filter": [
                        {
                            "k": "provider",
                            "v": "aws",
                            "o": "eq"
                        },
                        {
                            "v": "EC2",
                            "k": "cloud_service_group",
                            "o": "eq"
                        },
                        {
                            "k": "cloud_service_type",
                            "v": "Instance",
                            "o": "eq"
                        }
                    ],
                    "keyword": "test"
                }
            ],
            "options": {
                "raw_filter": [
                    [
                        "test"
                    ]
                ]
            },
            "tags": {},
            "project_id": "project-18655561c535",
            "domain_id": "domain-58010aa2e451",
            "created_at": "2021-06-01T10:23:20.537Z"
        }
    ],
    "total_count": 2
}
```
{% endtab %}
{% endtabs %}
 
 

 
### stat
> **POST** /inventory/v1/resource-group/stat
>


| Type | Message |
| :--- | :--- |
| Request | [ResourceGroupStatQuery](resource-group.md#resourcegroupstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### CreateResourceGroupRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| name |string|✔| |
| resources |[list of Resource](resource-group.md#resource)|✔| |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| project_id |string|✔| |
| domain_id |string|✔| |

### GetResourceGroupRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| resource_group_id |string|✔| |
| domain_id |string|✔| |
| only |list of string|✘| |

### Resource
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| resource_type |string|✔| |
| filter |[google.protobuf.ListValue](https://developers.google.com/protocol-buffers/docs/reference/overview)|✘| |
| keyword |string|✘| |

### ResourceGroupInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| resource_group_id |string | |
| name |string | |
| resources |[list of Resource](resource-group.md#resource) | |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |
| project_id |string | |
| domain_id |string | |
| created_at |string | |

### ResourceGroupQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|✘| |
| resource_group_id |string|✘| |
| name |string|✘| |
| project_id |string|✘| |
| domain_id |string|✔| |

### ResourceGroupRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| resource_group_id |string|✔| |
| domain_id |string|✔| |

### ResourceGroupStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✔| |
| domain_id |string|✔| |

### ResourceGroupsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of ResourceGroupInfo](resource-group.md#resourcegroupinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### UpdateResourceGroupRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| resource_group_id |string|✔| |
| name |string|✘| |
| resources |[list of Resource](resource-group.md#resource)|✘| |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| release_project |bool|✘| |
| project_id |string|✘| |
| domain_id |string|✔| |
