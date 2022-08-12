---
description: A Resource is a resource used for analysis on all microservices used in Cloudforet.
---
# Resource

>  **Package : spaceone.api.statistics.v1**

## Resource

{% hint style="info" %}
**Resource Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**stat**](resource.md#stat)|   [ResourceStatRequest](resource.md#resourcestatrequest) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
### stat
> **POST** /statistics/v1/resources/stat
>

> Enables data preprocessing of different services. Although limited, it is possible to create not only basic queries but also data suitable for users' needs, such as joins between two tables created by the query, handling missing values, and sorting.

| Type | Message |
| :--- | :--- |
| Request | [ResourceStatRequest](resource.md#resourcestatrequest) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "aggregate": [
        {
            "query": {
                "resource_type": "inventory.CloudServiceType",
                "query": {
                    "filter": [
                        {
                            "k": "labels",
                            "v": [
                                "Server"
                            ],
                            "o": "in"
                        },
                        {
                            "k": "is_primary",
                            "v": true,
                            "o": "eq"
                        }
                    ],
                    "aggregate": [
                        {
                            "group": {
                                "keys": [
                                    {
                                        "key": "cloud_service_type_id",
                                        "name": "cloud_service_type_id"
                                    },
                                    {
                                        "key": "name",
                                        "name": "cloud_service_type"
                                    },
                                    {
                                        "key": "group",
                                        "name": "cloud_service_group"
                                    },
                                    {
                                        "key": "provider",
                                        "name": "provider"
                                    },
                                    {
                                        "key": "cloud_service_type_id",
                                        "name": "cloud_service_type_id"
                                    }
                                ],
                                "fields": [
                                    {
                                        "key": "tags",
                                        "name": "tags",
                                        "operator": "first"
                                    },
                                    {
                                        "key": "labels",
                                        "name": "labels",
                                        "operator": "first"
                                    }
                                ]
                            }
                        }
                    ]
                }
            }
        },
        {
            "join": {
                "resource_type": "inventory.CloudService",
                "query": {
                    "filter": [
                        {
                            "k": "ref_cloud_service_type.cloud_service_type_id",
                            "v": [
                                "cloud-svc-type-58c926b19aca",
                                "cloud-svc-type-c7e5bc38d911",
                                "cloud-svc-type-8dd4d7a13b95",
                                "cloud-svc-type-719e705cb529",
                                "cloud-svc-type-50bd62cf6e0e"
                            ],
                            "o": "in"
                        }
                    ],
                    "aggregate": [
                        {
                            "group": {
                                "keys": [
                                    {
                                        "key": "cloud_service_type",
                                        "name": "cloud_service_type"
                                    },
                                    {
                                        "key": "cloud_service_group",
                                        "name": "cloud_service_group"
                                    },
                                    {
                                        "key": "provider",
                                        "name": "provider"
                                    }
                                ],
                                "fields": [
                                    {
                                        "name": "count",
                                        "operator": "count"
                                    }
                                ]
                            }
                        }
                    ]
                },
                "keys": [
                    "cloud_service_type",
                    "cloud_service_group",
                    "provider"
                ]
            }
        },
        {
            "fill_na": {
                "data": {
                    "count": 0.0
                }
            }
        },
        {
            "formula": {
                "query": "count > 0"
            }
        },
        {
            "sort": {
                "key": "count",
                "desc": true
            }
        }
    ],
    "domain_id": "domain-58010aa2e451"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "total_count": 5.0,
    "results": [
        {
            "labels": [
                "Compute",
                "Server"
            ],
            "cloud_service_type_id": "cloud-svc-type-58c926b19aca",
            "cloud_service_type": "Instance",
            "count": 44.0,
            "tags": [
                {
                    "key": "spaceone:icon",
                    "value": "https://spaceone-custom-assets.s3.ap-northeast-2.amazonaws.com/console-assets/icons/aws-ec2.svg"
                }
            ],
            "provider": "aws",
            "cloud_service_group": "EC2"
        },
        {
            "tags": [
                {
                    "key": "spaceone:icon",
                    "value": "https://spaceone-custom-assets.s3.ap-northeast-2.amazonaws.com/console-assets/icons/cloud-services/openstack/openstack_compute.svg"
                },
                {
                    "key": "spaceone:display_name",
                    "value": "Instance"
                }
            ],
            "cloud_service_group": "Compute",
            "cloud_service_type": "Instance",
            "provider": "openstack",
            "count": 12.0,
            "labels": [
                "Compute",
                "Server"
            ],
            "cloud_service_type_id": "cloud-svc-type-50bd62cf6e0e"
        },
        {
            "cloud_service_type": "Node",
            "count": 8.0,
            "provider": "kubernetes",
            "cloud_service_type_id": "cloud-svc-type-719e705cb529",
            "cloud_service_group": "Cluster",
            "tags": [
                {
                    "value": "https://spaceone-custom-assets.s3.ap-northeast-2.amazonaws.com/console-assets/icons/cloud-services/kubernetes/node.svg",
                    "key": "spaceone:icon"
                }
            ],
            "labels": [
                "Compute",
                "Server",
                "Container"
            ]
        },
        {
            "cloud_service_type_id": "cloud-svc-type-8dd4d7a13b95",
            "cloud_service_type": "Instance",
            "cloud_service_group": "ComputeEngine",
            "labels": [
                "Compute",
                "Server"
            ],
            "tags": [
                {
                    "key": "spaceone:icon",
                    "value": "https://spaceone-custom-assets.s3.ap-northeast-2.amazonaws.com/console-assets/icons/cloud-services/google_cloud/Compute_Engine.svg"
                }
            ],
            "count": 5.0,
            "provider": "google_cloud"
        },
        {
            "tags": [
                {
                    "value": "https://spaceone-custom-assets.s3.ap-northeast-2.amazonaws.com/console-assets/icons/azure-vm.svg",
                    "key": "spaceone:icon"
                }
            ],
            "cloud_service_type": "VirtualMachine",
            "cloud_service_group": "Compute",
            "count": 2.0,
            "provider": "azure",
            "cloud_service_type_id": "cloud-svc-type-c7e5bc38d911",
            "labels": [
                "Compute",
                "Server"
            ]
        }
    ]
}
```
{% endtab %}
{% endtabs %}


## 

## Message

### ResourceStatRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| aggregate |[list of StatAggregate](resource.md#stataggregate)|✔| |
| page |[StatPage](resource.md#statpage)|✘| |
| domain_id |string|✔| |

### SortKey
| Field | Type |  Description |
| :--- | :--- | :--- |
| key |string | |
| desc |bool | |

### StatAggregate
| Field | Type |  Description |
| :--- | :--- | :--- |
| query |[StatAggregateQuery](resource.md#stataggregatequery) | |
| join |[StatAggregateJoin](resource.md#stataggregatejoin) | |
| concat |[StatAggregateConcat](resource.md#stataggregateconcat) | |
| sort |[StatAggregateSort](resource.md#stataggregatesort) | |
| formula |[StatAggregateFormula](resource.md#stataggregateformula) | |
| fill_na |[StatAggregateFillNA](resource.md#stataggregatefillna) | |

### StatAggregateConcat
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| resource_type |string|✔| |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✔| |
| extend_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |

### StatAggregateFillNA
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✔| |

### StatAggregateFormula
| Field | Type |  Description |
| :--- | :--- | :--- |
| eval |string | |
| query |string | |

### StatAggregateJoin
<table>
  <thead>
    <tr>
      <th style="text-align:left; width:100px;">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:center">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left; width:100px;">resource_type</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">query</td>
      <td style="text-align:left"><a href="https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query">spaceone.api.core.v1.StatisticsQuery</a></td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">extend_data</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">type</td>
      <td style="text-align:left"><ul>
          	<li>LEFT</li>
          	<li>RIGHT</li>
          	<li>OUTER</li>
          	<li>INNER</li>
        </ul></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">keys</td>
      <td style="text-align:left">list of string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### StatAggregateQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| resource_type |string|✔| |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✔| |
| extend_data |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |

### StatAggregateSort
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| key |string|✘| |
| desc |bool|✘| |
| keys |[list of SortKey](resource.md#sortkey)|✘| |

### StatPage
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| start |[uint32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)|✘| |
| limit |[uint32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)|✔| |
