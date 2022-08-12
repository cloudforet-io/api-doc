---
description: A Schedule is a time schedule of when a User will use a query.
---
# Schedule

>  **Package : spaceone.api.statistics.v1**

## Schedule

{% hint style="info" %}
**Schedule Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**add**](schedule.md#add)|   [AddScheduleRequest](schedule.md#addschedulerequest) |   [ScheduleInfo](schedule.md#scheduleinfo) |
| [**update**](schedule.md#update)|   [UpdateScheduleRequest](schedule.md#updateschedulerequest) |   [ScheduleInfo](schedule.md#scheduleinfo) |
| [**enable**](schedule.md#enable)|   [ScheduleRequest](schedule.md#schedulerequest) |   [ScheduleInfo](schedule.md#scheduleinfo) |
| [**disable**](schedule.md#disable)|   [ScheduleRequest](schedule.md#schedulerequest) |   [ScheduleInfo](schedule.md#scheduleinfo) |
| [**delete**](schedule.md#delete)|   [ScheduleRequest](schedule.md#schedulerequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**get**](schedule.md#get)|   [GetScheduleRequest](schedule.md#getschedulerequest) |   [ScheduleInfo](schedule.md#scheduleinfo) |
| [**list**](schedule.md#list)|   [ScheduleQuery](schedule.md#schedulequery) |   [SchedulesInfo](schedule.md#schedulesinfo) |
| [**stat**](schedule.md#stat)|   [ScheduleStatQuery](schedule.md#schedulestatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
### add
> **POST** /statistics/v1/schedules
>

> Adds a new Schedule. When creating, `topic` and queries to be used should be specified. The time interval of the Schedule should be also specified to run queries repeatedly. The run set by Schedule starts every hour on the hour.

| Type | Message |
| :--- | :--- |
| Request | [AddScheduleRequest](schedule.md#addschedulerequest) |
| Response |  [ScheduleInfo](schedule.md#scheduleinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "topic": "daily_cloud_service_summary_test",
    "options": {
        "aggregate": [
            {
                "query": {
                    "extend_data": {
                        "label": "Server"
                    },
                    "query": {
                        "filter": [
                            {
                                "key": "ref_cloud_service_type.is_primary",
                                "value": true,
                                "operator": "eq"
                            },
                            {
                                "value": "Server",
                                "operator": "eq",
                                "key": "ref_cloud_service_type.labels"
                            }
                        ],
                        "aggregate": [
                            {
                                "group": {
                                    "fields": [
                                        {
                                            "name": "value",
                                            "operator": "count"
                                        }
                                    ],
                                    "keys": [
                                        {
                                            "name": "project_id",
                                            "key": "project_id"
                                        },
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
                                    ]
                                }
                            }
                        ]
                    },
                    "resource_type": "inventory.CloudService"
                }
            },
            {
                "concat": {
                    "resource_type": "inventory.CloudService",
                    "query": {
                        "aggregate": [
                            {
                                "group": {
                                    "keys": [
                                        {
                                            "key": "project_id",
                                            "name": "project_id"
                                        },
                                        {
                                            "name": "cloud_service_type",
                                            "key": "cloud_service_type"
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
                                            "name": "value",
                                            "operator": "count"
                                        }
                                    ]
                                }
                            }
                        ],
                        "filter": [
                            {
                                "value": true,
                                "operator": "eq",
                                "key": "ref_cloud_service_type.is_primary"
                            },
                            {
                                "value": "Database",
                                "operator": "eq",
                                "key": "ref_cloud_service_type.labels"
                            }
                        ]
                    },
                    "extend_data": {
                        "label": "Database"
                    }
                }
            },
            {
                "concat": {
                    "resource_type": "inventory.CloudService",
                    "extend_data": {
                        "label": "Container"
                    },
                    "query": {
                        "filter": [
                            {
                                "value": true,
                                "key": "ref_cloud_service_type.is_primary",
                                "operator": "eq"
                            },
                            {
                                "key": "ref_cloud_service_type.labels",
                                "value": "Container",
                                "operator": "eq"
                            }
                        ],
                        "aggregate": [
                            {
                                "group": {
                                    "fields": [
                                        {
                                            "name": "value",
                                            "operator": "count"
                                        }
                                    ],
                                    "keys": [
                                        {
                                            "key": "project_id",
                                            "name": "project_id"
                                        },
                                        {
                                            "name": "cloud_service_type",
                                            "key": "cloud_service_type"
                                        },
                                        {
                                            "name": "cloud_service_group",
                                            "key": "cloud_service_group"
                                        },
                                        {
                                            "key": "provider",
                                            "name": "provider"
                                        }
                                    ]
                                }
                            }
                        ]
                    }
                }
            },
            {
                "concat": {
                    "extend_data": {
                        "label": "Networking"
                    },
                    "query": {
                        "aggregate": [
                            {
                                "group": {
                                    "keys": [
                                        {
                                            "name": "project_id",
                                            "key": "project_id"
                                        },
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
                                            "name": "value",
                                            "operator": "count"
                                        }
                                    ]
                                }
                            }
                        ],
                        "filter": [
                            {
                                "key": "ref_cloud_service_type.is_primary",
                                "operator": "eq",
                                "value": true
                            },
                            {
                                "key": "ref_cloud_service_type.labels",
                                "value": "Networking",
                                "operator": "eq"
                            }
                        ]
                    },
                    "resource_type": "inventory.CloudService"
                }
            },
            {
                "concat": {
                    "resource_type": "inventory.CloudService",
                    "query": {
                        "filter": [
                            {
                                "key": "ref_cloud_service_type.is_primary",
                                "value": true,
                                "operator": "eq"
                            },
                            {
                                "operator": "eq",
                                "value": "Security",
                                "key": "ref_cloud_service_type.labels"
                            }
                        ],
                        "aggregate": [
                            {
                                "group": {
                                    "keys": [
                                        {
                                            "key": "project_id",
                                            "name": "project_id"
                                        },
                                        {
                                            "key": "cloud_service_type",
                                            "name": "cloud_service_type"
                                        },
                                        {
                                            "name": "cloud_service_group",
                                            "key": "cloud_service_group"
                                        },
                                        {
                                            "key": "provider",
                                            "name": "provider"
                                        }
                                    ],
                                    "fields": [
                                        {
                                            "name": "value",
                                            "operator": "count"
                                        }
                                    ]
                                }
                            }
                        ]
                    },
                    "extend_data": {
                        "label": "Security"
                    }
                }
            },
            {
                "concat": {
                    "resource_type": "inventory.CloudService",
                    "extend_data": {
                        "label": "Analytics"
                    },
                    "query": {
                        "filter": [
                            {
                                "value": true,
                                "key": "ref_cloud_service_type.is_primary",
                                "operator": "eq"
                            },
                            {
                                "operator": "eq",
                                "value": "Analytics",
                                "key": "ref_cloud_service_type.labels"
                            }
                        ],
                        "aggregate": [
                            {
                                "group": {
                                    "fields": [
                                        {
                                            "operator": "count",
                                            "name": "value"
                                        }
                                    ],
                                    "keys": [
                                        {
                                            "name": "project_id",
                                            "key": "project_id"
                                        },
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
                                    ]
                                }
                            }
                        ]
                    }
                }
            },
            {
                "concat": {
                    "resource_type": "inventory.CloudService",
                    "extend_data": {
                        "label": "All"
                    },
                    "query": {
                        "aggregate": [
                            {
                                "group": {
                                    "keys": [
                                        {
                                            "name": "project_id",
                                            "key": "project_id"
                                        },
                                        {
                                            "name": "cloud_service_type",
                                            "key": "cloud_service_type"
                                        },
                                        {
                                            "name": "cloud_service_group",
                                            "key": "cloud_service_group"
                                        },
                                        {
                                            "key": "provider",
                                            "name": "provider"
                                        }
                                    ],
                                    "fields": [
                                        {
                                            "operator": "count",
                                            "name": "value"
                                        }
                                    ]
                                }
                            }
                        ],
                        "filter": [
                            {
                                "key": "ref_cloud_service_type.is_primary",
                                "operator": "eq",
                                "value": true
                            }
                        ]
                    }
                }
            },
            {
                "concat": {
                    "query": {
                        "filter": [
                            {
                                "value": true,
                                "operator": "eq",
                                "key": "ref_cloud_service_type.is_major"
                            },
                            {
                                "value": "Storage",
                                "operator": "eq",
                                "key": "ref_cloud_service_type.labels"
                            }
                        ],
                        "aggregate": [
                            {
                                "group": {
                                    "fields": [
                                        {
                                            "name": "value",
                                            "key": "data.size",
                                            "operator": "sum"
                                        }
                                    ],
                                    "keys": [
                                        {
                                            "name": "project_id",
                                            "key": "project_id"
                                        },
                                        {
                                            "name": "cloud_service_type",
                                            "key": "cloud_service_type"
                                        },
                                        {
                                            "key": "cloud_service_group",
                                            "name": "cloud_service_group"
                                        },
                                        {
                                            "key": "provider",
                                            "name": "provider"
                                        }
                                    ]
                                }
                            }
                        ]
                    },
                    "resource_type": "inventory.CloudService",
                    "extend_data": {
                        "label": "Storage"
                    }
                }
            }
        ]
    },
    "schedule": {
        "hours": [
            1
        ]
    },
    "tags": {},
    "domain_id": "domain-58010aa2e451"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "schedule_id": "sch-65bb6b55d162",
    "topic": "daily_cloud_service_summary_test",
    "state": "ENABLED",
    "options": {
        "aggregate": [
            {
                "query": {
                    "extend_data": {
                        "label": "Server"
                    },
                    "resource_type": "inventory.CloudService",
                    "query": {
                        "filter": [
                            {
                                "key": "ref_cloud_service_type.is_primary",
                                "value": true,
                                "operator": "eq"
                            },
                            {
                                "operator": "eq",
                                "key": "ref_cloud_service_type.labels",
                                "value": "Server"
                            }
                        ],
                        "aggregate": [
                            {
                                "group": {
                                    "fields": [
                                        {
                                            "operator": "count",
                                            "name": "value"
                                        }
                                    ],
                                    "keys": [
                                        {
                                            "name": "project_id",
                                            "key": "project_id"
                                        },
                                        {
                                            "name": "cloud_service_type",
                                            "key": "cloud_service_type"
                                        },
                                        {
                                            "key": "cloud_service_group",
                                            "name": "cloud_service_group"
                                        },
                                        {
                                            "key": "provider",
                                            "name": "provider"
                                        }
                                    ]
                                }
                            }
                        ]
                    }
                }
            },
            {
                "concat": {
                    "query": {
                        "aggregate": [
                            {
                                "group": {
                                    "fields": [
                                        {
                                            "operator": "count",
                                            "name": "value"
                                        }
                                    ],
                                    "keys": [
                                        {
                                            "name": "project_id",
                                            "key": "project_id"
                                        },
                                        {
                                            "name": "cloud_service_type",
                                            "key": "cloud_service_type"
                                        },
                                        {
                                            "key": "cloud_service_group",
                                            "name": "cloud_service_group"
                                        },
                                        {
                                            "key": "provider",
                                            "name": "provider"
                                        }
                                    ]
                                }
                            }
                        ],
                        "filter": [
                            {
                                "operator": "eq",
                                "value": true,
                                "key": "ref_cloud_service_type.is_primary"
                            },
                            {
                                "operator": "eq",
                                "key": "ref_cloud_service_type.labels",
                                "value": "Database"
                            }
                        ]
                    },
                    "resource_type": "inventory.CloudService",
                    "extend_data": {
                        "label": "Database"
                    }
                }
            },
            {
                "concat": {
                    "resource_type": "inventory.CloudService",
                    "query": {
                        "aggregate": [
                            {
                                "group": {
                                    "fields": [
                                        {
                                            "operator": "count",
                                            "name": "value"
                                        }
                                    ],
                                    "keys": [
                                        {
                                            "key": "project_id",
                                            "name": "project_id"
                                        },
                                        {
                                            "name": "cloud_service_type",
                                            "key": "cloud_service_type"
                                        },
                                        {
                                            "key": "cloud_service_group",
                                            "name": "cloud_service_group"
                                        },
                                        {
                                            "name": "provider",
                                            "key": "provider"
                                        }
                                    ]
                                }
                            }
                        ],
                        "filter": [
                            {
                                "key": "ref_cloud_service_type.is_primary",
                                "value": true,
                                "operator": "eq"
                            },
                            {
                                "operator": "eq",
                                "key": "ref_cloud_service_type.labels",
                                "value": "Container"
                            }
                        ]
                    },
                    "extend_data": {
                        "label": "Container"
                    }
                }
            },
            {
                "concat": {
                    "query": {
                        "aggregate": [
                            {
                                "group": {
                                    "keys": [
                                        {
                                            "key": "project_id",
                                            "name": "project_id"
                                        },
                                        {
                                            "name": "cloud_service_type",
                                            "key": "cloud_service_type"
                                        },
                                        {
                                            "name": "cloud_service_group",
                                            "key": "cloud_service_group"
                                        },
                                        {
                                            "key": "provider",
                                            "name": "provider"
                                        }
                                    ],
                                    "fields": [
                                        {
                                            "operator": "count",
                                            "name": "value"
                                        }
                                    ]
                                }
                            }
                        ],
                        "filter": [
                            {
                                "key": "ref_cloud_service_type.is_primary",
                                "operator": "eq",
                                "value": true
                            },
                            {
                                "key": "ref_cloud_service_type.labels",
                                "operator": "eq",
                                "value": "Networking"
                            }
                        ]
                    },
                    "resource_type": "inventory.CloudService",
                    "extend_data": {
                        "label": "Networking"
                    }
                }
            },
            {
                "concat": {
                    "resource_type": "inventory.CloudService",
                    "extend_data": {
                        "label": "Security"
                    },
                    "query": {
                        "filter": [
                            {
                                "operator": "eq",
                                "key": "ref_cloud_service_type.is_primary",
                                "value": true
                            },
                            {
                                "operator": "eq",
                                "key": "ref_cloud_service_type.labels",
                                "value": "Security"
                            }
                        ],
                        "aggregate": [
                            {
                                "group": {
                                    "keys": [
                                        {
                                            "name": "project_id",
                                            "key": "project_id"
                                        },
                                        {
                                            "name": "cloud_service_type",
                                            "key": "cloud_service_type"
                                        },
                                        {
                                            "name": "cloud_service_group",
                                            "key": "cloud_service_group"
                                        },
                                        {
                                            "key": "provider",
                                            "name": "provider"
                                        }
                                    ],
                                    "fields": [
                                        {
                                            "name": "value",
                                            "operator": "count"
                                        }
                                    ]
                                }
                            }
                        ]
                    }
                }
            },
            {
                "concat": {
                    "resource_type": "inventory.CloudService",
                    "query": {
                        "filter": [
                            {
                                "key": "ref_cloud_service_type.is_primary",
                                "value": true,
                                "operator": "eq"
                            },
                            {
                                "key": "ref_cloud_service_type.labels",
                                "value": "Analytics",
                                "operator": "eq"
                            }
                        ],
                        "aggregate": [
                            {
                                "group": {
                                    "keys": [
                                        {
                                            "key": "project_id",
                                            "name": "project_id"
                                        },
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
                                            "operator": "count",
                                            "name": "value"
                                        }
                                    ]
                                }
                            }
                        ]
                    },
                    "extend_data": {
                        "label": "Analytics"
                    }
                }
            },
            {
                "concat": {
                    "extend_data": {
                        "label": "All"
                    },
                    "resource_type": "inventory.CloudService",
                    "query": {
                        "filter": [
                            {
                                "key": "ref_cloud_service_type.is_primary",
                                "value": true,
                                "operator": "eq"
                            }
                        ],
                        "aggregate": [
                            {
                                "group": {
                                    "fields": [
                                        {
                                            "name": "value",
                                            "operator": "count"
                                        }
                                    ],
                                    "keys": [
                                        {
                                            "key": "project_id",
                                            "name": "project_id"
                                        },
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
                                    ]
                                }
                            }
                        ]
                    }
                }
            },
            {
                "concat": {
                    "resource_type": "inventory.CloudService",
                    "query": {
                        "aggregate": [
                            {
                                "group": {
                                    "fields": [
                                        {
                                            "operator": "sum",
                                            "name": "value",
                                            "key": "data.size"
                                        }
                                    ],
                                    "keys": [
                                        {
                                            "name": "project_id",
                                            "key": "project_id"
                                        },
                                        {
                                            "key": "cloud_service_type",
                                            "name": "cloud_service_type"
                                        },
                                        {
                                            "name": "cloud_service_group",
                                            "key": "cloud_service_group"
                                        },
                                        {
                                            "name": "provider",
                                            "key": "provider"
                                        }
                                    ]
                                }
                            }
                        ],
                        "filter": [
                            {
                                "operator": "eq",
                                "key": "ref_cloud_service_type.is_major",
                                "value": true
                            },
                            {
                                "value": "Storage",
                                "operator": "eq",
                                "key": "ref_cloud_service_type.labels"
                            }
                        ]
                    },
                    "extend_data": {
                        "label": "Storage"
                    }
                }
            }
        ]
    },
    "schedule": {
        "hours": [
            1
        ]
    },
    "tags": {},
    "domain_id": "domain-58010aa2e451",
    "created_at": "2022-07-26T02:08:48.233Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### update
> **PUT** /statistics/v1/schedule/{schedule_id}
>

> Updates a specific Schedule. You can make changes in Schedule settings, including time intervals.

| Type | Message |
| :--- | :--- |
| Request | [UpdateScheduleRequest](schedule.md#updateschedulerequest) |
| Response |  [ScheduleInfo](schedule.md#scheduleinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "schedule_id": "sch-65bb6b55d162",
    "schedule": {
        "hours": [
            2
        ]
    },
    "tags": {
        "a": "b"
    },
    "domain_id": "domain-58010aa2e451"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "schedule_id": "sch-65bb6b55d162",
    "topic": "daily_cloud_service_summary_test",
    "state": "ENABLED",
    "options": {
        "aggregate": [
            {
                "query": {
                    "resource_type": "inventory.CloudService",
                    "extend_data": {
                        "label": "Server"
                    },
                    "query": {
                        "filter": [
                            {
                                "value": true,
                                "operator": "eq",
                                "key": "ref_cloud_service_type.is_primary"
                            },
                            {
                                "key": "ref_cloud_service_type.labels",
                                "value": "Server",
                                "operator": "eq"
                            }
                        ],
                        "aggregate": [
                            {
                                "group": {
                                    "keys": [
                                        {
                                            "name": "project_id",
                                            "key": "project_id"
                                        },
                                        {
                                            "key": "cloud_service_type",
                                            "name": "cloud_service_type"
                                        },
                                        {
                                            "name": "cloud_service_group",
                                            "key": "cloud_service_group"
                                        },
                                        {
                                            "key": "provider",
                                            "name": "provider"
                                        }
                                    ],
                                    "fields": [
                                        {
                                            "operator": "count",
                                            "name": "value"
                                        }
                                    ]
                                }
                            }
                        ]
                    }
                }
            },
            {
                "concat": {
                    "extend_data": {
                        "label": "Database"
                    },
                    "query": {
                        "aggregate": [
                            {
                                "group": {
                                    "fields": [
                                        {
                                            "operator": "count",
                                            "name": "value"
                                        }
                                    ],
                                    "keys": [
                                        {
                                            "key": "project_id",
                                            "name": "project_id"
                                        },
                                        {
                                            "name": "cloud_service_type",
                                            "key": "cloud_service_type"
                                        },
                                        {
                                            "name": "cloud_service_group",
                                            "key": "cloud_service_group"
                                        },
                                        {
                                            "name": "provider",
                                            "key": "provider"
                                        }
                                    ]
                                }
                            }
                        ],
                        "filter": [
                            {
                                "operator": "eq",
                                "value": true,
                                "key": "ref_cloud_service_type.is_primary"
                            },
                            {
                                "value": "Database",
                                "key": "ref_cloud_service_type.labels",
                                "operator": "eq"
                            }
                        ]
                    },
                    "resource_type": "inventory.CloudService"
                }
            },
            {
                "concat": {
                    "extend_data": {
                        "label": "Container"
                    },
                    "query": {
                        "filter": [
                            {
                                "value": true,
                                "key": "ref_cloud_service_type.is_primary",
                                "operator": "eq"
                            },
                            {
                                "operator": "eq",
                                "key": "ref_cloud_service_type.labels",
                                "value": "Container"
                            }
                        ],
                        "aggregate": [
                            {
                                "group": {
                                    "keys": [
                                        {
                                            "key": "project_id",
                                            "name": "project_id"
                                        },
                                        {
                                            "name": "cloud_service_type",
                                            "key": "cloud_service_type"
                                        },
                                        {
                                            "name": "cloud_service_group",
                                            "key": "cloud_service_group"
                                        },
                                        {
                                            "name": "provider",
                                            "key": "provider"
                                        }
                                    ],
                                    "fields": [
                                        {
                                            "operator": "count",
                                            "name": "value"
                                        }
                                    ]
                                }
                            }
                        ]
                    },
                    "resource_type": "inventory.CloudService"
                }
            },
            {
                "concat": {
                    "resource_type": "inventory.CloudService",
                    "query": {
                        "aggregate": [
                            {
                                "group": {
                                    "fields": [
                                        {
                                            "name": "value",
                                            "operator": "count"
                                        }
                                    ],
                                    "keys": [
                                        {
                                            "key": "project_id",
                                            "name": "project_id"
                                        },
                                        {
                                            "name": "cloud_service_type",
                                            "key": "cloud_service_type"
                                        },
                                        {
                                            "key": "cloud_service_group",
                                            "name": "cloud_service_group"
                                        },
                                        {
                                            "key": "provider",
                                            "name": "provider"
                                        }
                                    ]
                                }
                            }
                        ],
                        "filter": [
                            {
                                "operator": "eq",
                                "value": true,
                                "key": "ref_cloud_service_type.is_primary"
                            },
                            {
                                "operator": "eq",
                                "value": "Networking",
                                "key": "ref_cloud_service_type.labels"
                            }
                        ]
                    },
                    "extend_data": {
                        "label": "Networking"
                    }
                }
            },
            {
                "concat": {
                    "query": {
                        "filter": [
                            {
                                "value": true,
                                "key": "ref_cloud_service_type.is_primary",
                                "operator": "eq"
                            },
                            {
                                "key": "ref_cloud_service_type.labels",
                                "operator": "eq",
                                "value": "Security"
                            }
                        ],
                        "aggregate": [
                            {
                                "group": {
                                    "fields": [
                                        {
                                            "operator": "count",
                                            "name": "value"
                                        }
                                    ],
                                    "keys": [
                                        {
                                            "name": "project_id",
                                            "key": "project_id"
                                        },
                                        {
                                            "name": "cloud_service_type",
                                            "key": "cloud_service_type"
                                        },
                                        {
                                            "key": "cloud_service_group",
                                            "name": "cloud_service_group"
                                        },
                                        {
                                            "name": "provider",
                                            "key": "provider"
                                        }
                                    ]
                                }
                            }
                        ]
                    },
                    "extend_data": {
                        "label": "Security"
                    },
                    "resource_type": "inventory.CloudService"
                }
            },
            {
                "concat": {
                    "resource_type": "inventory.CloudService",
                    "extend_data": {
                        "label": "Analytics"
                    },
                    "query": {
                        "filter": [
                            {
                                "value": true,
                                "operator": "eq",
                                "key": "ref_cloud_service_type.is_primary"
                            },
                            {
                                "key": "ref_cloud_service_type.labels",
                                "operator": "eq",
                                "value": "Analytics"
                            }
                        ],
                        "aggregate": [
                            {
                                "group": {
                                    "fields": [
                                        {
                                            "name": "value",
                                            "operator": "count"
                                        }
                                    ],
                                    "keys": [
                                        {
                                            "name": "project_id",
                                            "key": "project_id"
                                        },
                                        {
                                            "key": "cloud_service_type",
                                            "name": "cloud_service_type"
                                        },
                                        {
                                            "name": "cloud_service_group",
                                            "key": "cloud_service_group"
                                        },
                                        {
                                            "key": "provider",
                                            "name": "provider"
                                        }
                                    ]
                                }
                            }
                        ]
                    }
                }
            },
            {
                "concat": {
                    "resource_type": "inventory.CloudService",
                    "extend_data": {
                        "label": "All"
                    },
                    "query": {
                        "filter": [
                            {
                                "key": "ref_cloud_service_type.is_primary",
                                "value": true,
                                "operator": "eq"
                            }
                        ],
                        "aggregate": [
                            {
                                "group": {
                                    "keys": [
                                        {
                                            "name": "project_id",
                                            "key": "project_id"
                                        },
                                        {
                                            "name": "cloud_service_type",
                                            "key": "cloud_service_type"
                                        },
                                        {
                                            "key": "cloud_service_group",
                                            "name": "cloud_service_group"
                                        },
                                        {
                                            "name": "provider",
                                            "key": "provider"
                                        }
                                    ],
                                    "fields": [
                                        {
                                            "name": "value",
                                            "operator": "count"
                                        }
                                    ]
                                }
                            }
                        ]
                    }
                }
            },
            {
                "concat": {
                    "extend_data": {
                        "label": "Storage"
                    },
                    "resource_type": "inventory.CloudService",
                    "query": {
                        "filter": [
                            {
                                "key": "ref_cloud_service_type.is_major",
                                "operator": "eq",
                                "value": true
                            },
                            {
                                "value": "Storage",
                                "key": "ref_cloud_service_type.labels",
                                "operator": "eq"
                            }
                        ],
                        "aggregate": [
                            {
                                "group": {
                                    "keys": [
                                        {
                                            "name": "project_id",
                                            "key": "project_id"
                                        },
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
                                            "key": "data.size",
                                            "name": "value",
                                            "operator": "sum"
                                        }
                                    ]
                                }
                            }
                        ]
                    }
                }
            }
        ]
    },
    "schedule": {
        "hours": [
            2
        ]
    },
    "tags": {
        "a": "b"
    },
    "domain_id": "domain-58010aa2e451",
    "created_at": "2022-07-26T02:08:48.233Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### enable
> **PUT** /statistics/v1/schedule/{schedule_id}/enable
>

> Enables a specific Schedule. If a Schedule is enabled, the query usage will be scheduled by the time interval specified.

| Type | Message |
| :--- | :--- |
| Request | [ScheduleRequest](schedule.md#schedulerequest) |
| Response |  [ScheduleInfo](schedule.md#scheduleinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "schedule_id": "sch-65bb6b55d162",
    "domain_id": "domain-58010aa2e451"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "schedule_id": "sch-65bb6b55d162",
    "topic": "daily_cloud_service_summary_test",
    "state": "ENABLED",
    "options": {
        "aggregate": [
            {
                "query": {
                    "query": {
                        "aggregate": [
                            {
                                "group": {
                                    "keys": [
                                        {
                                            "key": "project_id",
                                            "name": "project_id"
                                        },
                                        {
                                            "name": "cloud_service_type",
                                            "key": "cloud_service_type"
                                        },
                                        {
                                            "name": "cloud_service_group",
                                            "key": "cloud_service_group"
                                        },
                                        {
                                            "key": "provider",
                                            "name": "provider"
                                        }
                                    ],
                                    "fields": [
                                        {
                                            "name": "value",
                                            "operator": "count"
                                        }
                                    ]
                                }
                            }
                        ],
                        "filter": [
                            {
                                "value": true,
                                "operator": "eq",
                                "key": "ref_cloud_service_type.is_primary"
                            },
                            {
                                "value": "Server",
                                "operator": "eq",
                                "key": "ref_cloud_service_type.labels"
                            }
                        ]
                    },
                    "extend_data": {
                        "label": "Server"
                    },
                    "resource_type": "inventory.CloudService"
                }
            },
            {
                "concat": {
                    "resource_type": "inventory.CloudService",
                    "extend_data": {
                        "label": "Database"
                    },
                    "query": {
                        "filter": [
                            {
                                "operator": "eq",
                                "key": "ref_cloud_service_type.is_primary",
                                "value": true
                            },
                            {
                                "value": "Database",
                                "operator": "eq",
                                "key": "ref_cloud_service_type.labels"
                            }
                        ],
                        "aggregate": [
                            {
                                "group": {
                                    "fields": [
                                        {
                                            "operator": "count",
                                            "name": "value"
                                        }
                                    ],
                                    "keys": [
                                        {
                                            "name": "project_id",
                                            "key": "project_id"
                                        },
                                        {
                                            "key": "cloud_service_type",
                                            "name": "cloud_service_type"
                                        },
                                        {
                                            "name": "cloud_service_group",
                                            "key": "cloud_service_group"
                                        },
                                        {
                                            "key": "provider",
                                            "name": "provider"
                                        }
                                    ]
                                }
                            }
                        ]
                    }
                }
            },
            {
                "concat": {
                    "resource_type": "inventory.CloudService",
                    "extend_data": {
                        "label": "Container"
                    },
                    "query": {
                        "aggregate": [
                            {
                                "group": {
                                    "fields": [
                                        {
                                            "operator": "count",
                                            "name": "value"
                                        }
                                    ],
                                    "keys": [
                                        {
                                            "key": "project_id",
                                            "name": "project_id"
                                        },
                                        {
                                            "name": "cloud_service_type",
                                            "key": "cloud_service_type"
                                        },
                                        {
                                            "name": "cloud_service_group",
                                            "key": "cloud_service_group"
                                        },
                                        {
                                            "key": "provider",
                                            "name": "provider"
                                        }
                                    ]
                                }
                            }
                        ],
                        "filter": [
                            {
                                "key": "ref_cloud_service_type.is_primary",
                                "operator": "eq",
                                "value": true
                            },
                            {
                                "key": "ref_cloud_service_type.labels",
                                "value": "Container",
                                "operator": "eq"
                            }
                        ]
                    }
                }
            },
            {
                "concat": {
                    "extend_data": {
                        "label": "Networking"
                    },
                    "resource_type": "inventory.CloudService",
                    "query": {
                        "aggregate": [
                            {
                                "group": {
                                    "keys": [
                                        {
                                            "key": "project_id",
                                            "name": "project_id"
                                        },
                                        {
                                            "name": "cloud_service_type",
                                            "key": "cloud_service_type"
                                        },
                                        {
                                            "key": "cloud_service_group",
                                            "name": "cloud_service_group"
                                        },
                                        {
                                            "name": "provider",
                                            "key": "provider"
                                        }
                                    ],
                                    "fields": [
                                        {
                                            "operator": "count",
                                            "name": "value"
                                        }
                                    ]
                                }
                            }
                        ],
                        "filter": [
                            {
                                "key": "ref_cloud_service_type.is_primary",
                                "value": true,
                                "operator": "eq"
                            },
                            {
                                "key": "ref_cloud_service_type.labels",
                                "operator": "eq",
                                "value": "Networking"
                            }
                        ]
                    }
                }
            },
            {
                "concat": {
                    "resource_type": "inventory.CloudService",
                    "extend_data": {
                        "label": "Security"
                    },
                    "query": {
                        "aggregate": [
                            {
                                "group": {
                                    "fields": [
                                        {
                                            "operator": "count",
                                            "name": "value"
                                        }
                                    ],
                                    "keys": [
                                        {
                                            "name": "project_id",
                                            "key": "project_id"
                                        },
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
                                    ]
                                }
                            }
                        ],
                        "filter": [
                            {
                                "value": true,
                                "operator": "eq",
                                "key": "ref_cloud_service_type.is_primary"
                            },
                            {
                                "value": "Security",
                                "operator": "eq",
                                "key": "ref_cloud_service_type.labels"
                            }
                        ]
                    }
                }
            },
            {
                "concat": {
                    "extend_data": {
                        "label": "Analytics"
                    },
                    "resource_type": "inventory.CloudService",
                    "query": {
                        "filter": [
                            {
                                "operator": "eq",
                                "value": true,
                                "key": "ref_cloud_service_type.is_primary"
                            },
                            {
                                "operator": "eq",
                                "value": "Analytics",
                                "key": "ref_cloud_service_type.labels"
                            }
                        ],
                        "aggregate": [
                            {
                                "group": {
                                    "keys": [
                                        {
                                            "name": "project_id",
                                            "key": "project_id"
                                        },
                                        {
                                            "key": "cloud_service_type",
                                            "name": "cloud_service_type"
                                        },
                                        {
                                            "name": "cloud_service_group",
                                            "key": "cloud_service_group"
                                        },
                                        {
                                            "key": "provider",
                                            "name": "provider"
                                        }
                                    ],
                                    "fields": [
                                        {
                                            "name": "value",
                                            "operator": "count"
                                        }
                                    ]
                                }
                            }
                        ]
                    }
                }
            },
            {
                "concat": {
                    "extend_data": {
                        "label": "All"
                    },
                    "query": {
                        "filter": [
                            {
                                "value": true,
                                "key": "ref_cloud_service_type.is_primary",
                                "operator": "eq"
                            }
                        ],
                        "aggregate": [
                            {
                                "group": {
                                    "keys": [
                                        {
                                            "key": "project_id",
                                            "name": "project_id"
                                        },
                                        {
                                            "name": "cloud_service_type",
                                            "key": "cloud_service_type"
                                        },
                                        {
                                            "name": "cloud_service_group",
                                            "key": "cloud_service_group"
                                        },
                                        {
                                            "key": "provider",
                                            "name": "provider"
                                        }
                                    ],
                                    "fields": [
                                        {
                                            "name": "value",
                                            "operator": "count"
                                        }
                                    ]
                                }
                            }
                        ]
                    },
                    "resource_type": "inventory.CloudService"
                }
            },
            {
                "concat": {
                    "extend_data": {
                        "label": "Storage"
                    },
                    "resource_type": "inventory.CloudService",
                    "query": {
                        "aggregate": [
                            {
                                "group": {
                                    "fields": [
                                        {
                                            "key": "data.size",
                                            "name": "value",
                                            "operator": "sum"
                                        }
                                    ],
                                    "keys": [
                                        {
                                            "key": "project_id",
                                            "name": "project_id"
                                        },
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
                                    ]
                                }
                            }
                        ],
                        "filter": [
                            {
                                "value": true,
                                "key": "ref_cloud_service_type.is_major",
                                "operator": "eq"
                            },
                            {
                                "value": "Storage",
                                "key": "ref_cloud_service_type.labels",
                                "operator": "eq"
                            }
                        ]
                    }
                }
            }
        ]
    },
    "schedule": {
        "hours": [
            2
        ]
    },
    "tags": {
        "a": "b"
    },
    "domain_id": "domain-58010aa2e451",
    "created_at": "2022-07-26T02:08:48.233Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### disable
> **PUT** /statistics/v1/schedule/{schedule_id}/disable
>

> Disables a specific Schedule. If a Schedule is disabled, the query usage will not be scheduled.

| Type | Message |
| :--- | :--- |
| Request | [ScheduleRequest](schedule.md#schedulerequest) |
| Response |  [ScheduleInfo](schedule.md#scheduleinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "schedule_id": "sch-65bb6b55d162",
    "domain_id": "domain-58010aa2e451"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "schedule_id": "sch-65bb6b55d162",
    "topic": "daily_cloud_service_summary_test",
    "state": "DISABLED",
    "options": {
        "aggregate": [
            {
                "query": {
                    "query": {
                        "filter": [
                            {
                                "operator": "eq",
                                "key": "ref_cloud_service_type.is_primary",
                                "value": true
                            },
                            {
                                "operator": "eq",
                                "value": "Server",
                                "key": "ref_cloud_service_type.labels"
                            }
                        ],
                        "aggregate": [
                            {
                                "group": {
                                    "fields": [
                                        {
                                            "operator": "count",
                                            "name": "value"
                                        }
                                    ],
                                    "keys": [
                                        {
                                            "name": "project_id",
                                            "key": "project_id"
                                        },
                                        {
                                            "key": "cloud_service_type",
                                            "name": "cloud_service_type"
                                        },
                                        {
                                            "name": "cloud_service_group",
                                            "key": "cloud_service_group"
                                        },
                                        {
                                            "name": "provider",
                                            "key": "provider"
                                        }
                                    ]
                                }
                            }
                        ]
                    },
                    "extend_data": {
                        "label": "Server"
                    },
                    "resource_type": "inventory.CloudService"
                }
            },
            {
                "concat": {
                    "query": {
                        "filter": [
                            {
                                "operator": "eq",
                                "value": true,
                                "key": "ref_cloud_service_type.is_primary"
                            },
                            {
                                "operator": "eq",
                                "key": "ref_cloud_service_type.labels",
                                "value": "Database"
                            }
                        ],
                        "aggregate": [
                            {
                                "group": {
                                    "fields": [
                                        {
                                            "name": "value",
                                            "operator": "count"
                                        }
                                    ],
                                    "keys": [
                                        {
                                            "key": "project_id",
                                            "name": "project_id"
                                        },
                                        {
                                            "key": "cloud_service_type",
                                            "name": "cloud_service_type"
                                        },
                                        {
                                            "key": "cloud_service_group",
                                            "name": "cloud_service_group"
                                        },
                                        {
                                            "name": "provider",
                                            "key": "provider"
                                        }
                                    ]
                                }
                            }
                        ]
                    },
                    "resource_type": "inventory.CloudService",
                    "extend_data": {
                        "label": "Database"
                    }
                }
            },
            {
                "concat": {
                    "resource_type": "inventory.CloudService",
                    "extend_data": {
                        "label": "Container"
                    },
                    "query": {
                        "aggregate": [
                            {
                                "group": {
                                    "fields": [
                                        {
                                            "name": "value",
                                            "operator": "count"
                                        }
                                    ],
                                    "keys": [
                                        {
                                            "name": "project_id",
                                            "key": "project_id"
                                        },
                                        {
                                            "name": "cloud_service_type",
                                            "key": "cloud_service_type"
                                        },
                                        {
                                            "key": "cloud_service_group",
                                            "name": "cloud_service_group"
                                        },
                                        {
                                            "name": "provider",
                                            "key": "provider"
                                        }
                                    ]
                                }
                            }
                        ],
                        "filter": [
                            {
                                "operator": "eq",
                                "value": true,
                                "key": "ref_cloud_service_type.is_primary"
                            },
                            {
                                "key": "ref_cloud_service_type.labels",
                                "operator": "eq",
                                "value": "Container"
                            }
                        ]
                    }
                }
            },
            {
                "concat": {
                    "extend_data": {
                        "label": "Networking"
                    },
                    "query": {
                        "filter": [
                            {
                                "key": "ref_cloud_service_type.is_primary",
                                "operator": "eq",
                                "value": true
                            },
                            {
                                "operator": "eq",
                                "key": "ref_cloud_service_type.labels",
                                "value": "Networking"
                            }
                        ],
                        "aggregate": [
                            {
                                "group": {
                                    "fields": [
                                        {
                                            "name": "value",
                                            "operator": "count"
                                        }
                                    ],
                                    "keys": [
                                        {
                                            "key": "project_id",
                                            "name": "project_id"
                                        },
                                        {
                                            "name": "cloud_service_type",
                                            "key": "cloud_service_type"
                                        },
                                        {
                                            "name": "cloud_service_group",
                                            "key": "cloud_service_group"
                                        },
                                        {
                                            "name": "provider",
                                            "key": "provider"
                                        }
                                    ]
                                }
                            }
                        ]
                    },
                    "resource_type": "inventory.CloudService"
                }
            },
            {
                "concat": {
                    "resource_type": "inventory.CloudService",
                    "extend_data": {
                        "label": "Security"
                    },
                    "query": {
                        "aggregate": [
                            {
                                "group": {
                                    "fields": [
                                        {
                                            "operator": "count",
                                            "name": "value"
                                        }
                                    ],
                                    "keys": [
                                        {
                                            "key": "project_id",
                                            "name": "project_id"
                                        },
                                        {
                                            "key": "cloud_service_type",
                                            "name": "cloud_service_type"
                                        },
                                        {
                                            "name": "cloud_service_group",
                                            "key": "cloud_service_group"
                                        },
                                        {
                                            "name": "provider",
                                            "key": "provider"
                                        }
                                    ]
                                }
                            }
                        ],
                        "filter": [
                            {
                                "value": true,
                                "key": "ref_cloud_service_type.is_primary",
                                "operator": "eq"
                            },
                            {
                                "operator": "eq",
                                "value": "Security",
                                "key": "ref_cloud_service_type.labels"
                            }
                        ]
                    }
                }
            },
            {
                "concat": {
                    "resource_type": "inventory.CloudService",
                    "extend_data": {
                        "label": "Analytics"
                    },
                    "query": {
                        "aggregate": [
                            {
                                "group": {
                                    "fields": [
                                        {
                                            "name": "value",
                                            "operator": "count"
                                        }
                                    ],
                                    "keys": [
                                        {
                                            "name": "project_id",
                                            "key": "project_id"
                                        },
                                        {
                                            "key": "cloud_service_type",
                                            "name": "cloud_service_type"
                                        },
                                        {
                                            "name": "cloud_service_group",
                                            "key": "cloud_service_group"
                                        },
                                        {
                                            "key": "provider",
                                            "name": "provider"
                                        }
                                    ]
                                }
                            }
                        ],
                        "filter": [
                            {
                                "value": true,
                                "operator": "eq",
                                "key": "ref_cloud_service_type.is_primary"
                            },
                            {
                                "key": "ref_cloud_service_type.labels",
                                "value": "Analytics",
                                "operator": "eq"
                            }
                        ]
                    }
                }
            },
            {
                "concat": {
                    "extend_data": {
                        "label": "All"
                    },
                    "query": {
                        "aggregate": [
                            {
                                "group": {
                                    "keys": [
                                        {
                                            "key": "project_id",
                                            "name": "project_id"
                                        },
                                        {
                                            "key": "cloud_service_type",
                                            "name": "cloud_service_type"
                                        },
                                        {
                                            "name": "cloud_service_group",
                                            "key": "cloud_service_group"
                                        },
                                        {
                                            "key": "provider",
                                            "name": "provider"
                                        }
                                    ],
                                    "fields": [
                                        {
                                            "name": "value",
                                            "operator": "count"
                                        }
                                    ]
                                }
                            }
                        ],
                        "filter": [
                            {
                                "operator": "eq",
                                "key": "ref_cloud_service_type.is_primary",
                                "value": true
                            }
                        ]
                    },
                    "resource_type": "inventory.CloudService"
                }
            },
            {
                "concat": {
                    "query": {
                        "filter": [
                            {
                                "value": true,
                                "key": "ref_cloud_service_type.is_major",
                                "operator": "eq"
                            },
                            {
                                "key": "ref_cloud_service_type.labels",
                                "operator": "eq",
                                "value": "Storage"
                            }
                        ],
                        "aggregate": [
                            {
                                "group": {
                                    "fields": [
                                        {
                                            "key": "data.size",
                                            "operator": "sum",
                                            "name": "value"
                                        }
                                    ],
                                    "keys": [
                                        {
                                            "key": "project_id",
                                            "name": "project_id"
                                        },
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
                                    ]
                                }
                            }
                        ]
                    },
                    "resource_type": "inventory.CloudService",
                    "extend_data": {
                        "label": "Storage"
                    }
                }
            }
        ]
    },
    "schedule": {
        "hours": [
            2
        ]
    },
    "tags": {
        "a": "b"
    },
    "domain_id": "domain-58010aa2e451",
    "created_at": "2022-07-26T02:08:48.233Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### delete
> **DELETE** /statistics/v1/schedule/{schedule_id}
>

> Deletes a specific Schedule. You must specify the `schedule_id` of the Schedule to delete.

| Type | Message |
| :--- | :--- |
| Request | [ScheduleRequest](schedule.md#schedulerequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "schedule_id": "sch-3da9c9ed2ee2",
    "domain_id": "domain-58010aa2e451"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### get
> **GET** /statistics/v1/schedule/{schedule_id}
>

> Gets a specific Schedule. Prints detailed information about the Schedule, including the schedule interval and `state`.

| Type | Message |
| :--- | :--- |
| Request | [GetScheduleRequest](schedule.md#getschedulerequest) |
| Response |  [ScheduleInfo](schedule.md#scheduleinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "schedule_id": "sch-3da9c9ed2ee2",
    "domain_id": "domain-58010aa2e451"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "schedule_id": "sch-3da9c9ed2ee2",
    "topic": "daily_cloud_service_summary",
    "state": "ENABLED",
    "options": {
        "aggregate": [
            {
                "query": {
                    "resource_type": "inventory.CloudService",
                    "extend_data": {
                        "label": "Server"
                    },
                    "query": {
                        "filter": [
                            {
                                "value": true,
                                "operator": "eq",
                                "key": "ref_cloud_service_type.is_primary"
                            },
                            {
                                "value": "Server",
                                "key": "ref_cloud_service_type.labels",
                                "operator": "eq"
                            }
                        ],
                        "aggregate": [
                            {
                                "group": {
                                    "keys": [
                                        {
                                            "name": "project_id",
                                            "key": "project_id"
                                        },
                                        {
                                            "name": "cloud_service_type",
                                            "key": "cloud_service_type"
                                        },
                                        {
                                            "key": "cloud_service_group",
                                            "name": "cloud_service_group"
                                        },
                                        {
                                            "name": "provider",
                                            "key": "provider"
                                        }
                                    ],
                                    "fields": [
                                        {
                                            "operator": "count",
                                            "name": "value"
                                        }
                                    ]
                                }
                            }
                        ]
                    }
                }
            },
            {
                "concat": {
                    "extend_data": {
                        "label": "Database"
                    },
                    "resource_type": "inventory.CloudService",
                    "query": {
                        "aggregate": [
                            {
                                "group": {
                                    "fields": [
                                        {
                                            "name": "value",
                                            "operator": "count"
                                        }
                                    ],
                                    "keys": [
                                        {
                                            "key": "project_id",
                                            "name": "project_id"
                                        },
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
                                    ]
                                }
                            }
                        ],
                        "filter": [
                            {
                                "value": true,
                                "operator": "eq",
                                "key": "ref_cloud_service_type.is_primary"
                            },
                            {
                                "value": "Database",
                                "operator": "eq",
                                "key": "ref_cloud_service_type.labels"
                            }
                        ]
                    }
                }
            },
            {
                "concat": {
                    "query": {
                        "filter": [
                            {
                                "key": "ref_cloud_service_type.is_primary",
                                "operator": "eq",
                                "value": true
                            },
                            {
                                "operator": "eq",
                                "key": "ref_cloud_service_type.labels",
                                "value": "Container"
                            }
                        ],
                        "aggregate": [
                            {
                                "group": {
                                    "fields": [
                                        {
                                            "operator": "count",
                                            "name": "value"
                                        }
                                    ],
                                    "keys": [
                                        {
                                            "name": "project_id",
                                            "key": "project_id"
                                        },
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
                                    ]
                                }
                            }
                        ]
                    },
                    "resource_type": "inventory.CloudService",
                    "extend_data": {
                        "label": "Container"
                    }
                }
            },
            {
                "concat": {
                    "extend_data": {
                        "label": "Networking"
                    },
                    "resource_type": "inventory.CloudService",
                    "query": {
                        "aggregate": [
                            {
                                "group": {
                                    "fields": [
                                        {
                                            "name": "value",
                                            "operator": "count"
                                        }
                                    ],
                                    "keys": [
                                        {
                                            "key": "project_id",
                                            "name": "project_id"
                                        },
                                        {
                                            "key": "cloud_service_type",
                                            "name": "cloud_service_type"
                                        },
                                        {
                                            "name": "cloud_service_group",
                                            "key": "cloud_service_group"
                                        },
                                        {
                                            "key": "provider",
                                            "name": "provider"
                                        }
                                    ]
                                }
                            }
                        ],
                        "filter": [
                            {
                                "key": "ref_cloud_service_type.is_primary",
                                "operator": "eq",
                                "value": true
                            },
                            {
                                "operator": "eq",
                                "value": "Networking",
                                "key": "ref_cloud_service_type.labels"
                            }
                        ]
                    }
                }
            },
            {
                "concat": {
                    "resource_type": "inventory.CloudService",
                    "query": {
                        "filter": [
                            {
                                "value": true,
                                "operator": "eq",
                                "key": "ref_cloud_service_type.is_primary"
                            },
                            {
                                "operator": "eq",
                                "value": "Security",
                                "key": "ref_cloud_service_type.labels"
                            }
                        ],
                        "aggregate": [
                            {
                                "group": {
                                    "keys": [
                                        {
                                            "key": "project_id",
                                            "name": "project_id"
                                        },
                                        {
                                            "name": "cloud_service_type",
                                            "key": "cloud_service_type"
                                        },
                                        {
                                            "name": "cloud_service_group",
                                            "key": "cloud_service_group"
                                        },
                                        {
                                            "name": "provider",
                                            "key": "provider"
                                        }
                                    ],
                                    "fields": [
                                        {
                                            "operator": "count",
                                            "name": "value"
                                        }
                                    ]
                                }
                            }
                        ]
                    },
                    "extend_data": {
                        "label": "Security"
                    }
                }
            },
            {
                "concat": {
                    "query": {
                        "filter": [
                            {
                                "operator": "eq",
                                "value": true,
                                "key": "ref_cloud_service_type.is_primary"
                            },
                            {
                                "key": "ref_cloud_service_type.labels",
                                "operator": "eq",
                                "value": "Analytics"
                            }
                        ],
                        "aggregate": [
                            {
                                "group": {
                                    "keys": [
                                        {
                                            "name": "project_id",
                                            "key": "project_id"
                                        },
                                        {
                                            "name": "cloud_service_type",
                                            "key": "cloud_service_type"
                                        },
                                        {
                                            "key": "cloud_service_group",
                                            "name": "cloud_service_group"
                                        },
                                        {
                                            "name": "provider",
                                            "key": "provider"
                                        }
                                    ],
                                    "fields": [
                                        {
                                            "operator": "count",
                                            "name": "value"
                                        }
                                    ]
                                }
                            }
                        ]
                    },
                    "extend_data": {
                        "label": "Analytics"
                    },
                    "resource_type": "inventory.CloudService"
                }
            },
            {
                "concat": {
                    "extend_data": {
                        "label": "All"
                    },
                    "resource_type": "inventory.CloudService",
                    "query": {
                        "filter": [
                            {
                                "value": true,
                                "key": "ref_cloud_service_type.is_primary",
                                "operator": "eq"
                            }
                        ],
                        "aggregate": [
                            {
                                "group": {
                                    "fields": [
                                        {
                                            "operator": "count",
                                            "name": "value"
                                        }
                                    ],
                                    "keys": [
                                        {
                                            "name": "project_id",
                                            "key": "project_id"
                                        },
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
                                    ]
                                }
                            }
                        ]
                    }
                }
            },
            {
                "concat": {
                    "query": {
                        "filter": [
                            {
                                "operator": "eq",
                                "key": "ref_cloud_service_type.is_major",
                                "value": true
                            },
                            {
                                "value": "Storage",
                                "key": "ref_cloud_service_type.labels",
                                "operator": "eq"
                            }
                        ],
                        "aggregate": [
                            {
                                "group": {
                                    "keys": [
                                        {
                                            "key": "project_id",
                                            "name": "project_id"
                                        },
                                        {
                                            "name": "cloud_service_type",
                                            "key": "cloud_service_type"
                                        },
                                        {
                                            "key": "cloud_service_group",
                                            "name": "cloud_service_group"
                                        },
                                        {
                                            "name": "provider",
                                            "key": "provider"
                                        }
                                    ],
                                    "fields": [
                                        {
                                            "key": "data.size",
                                            "operator": "sum",
                                            "name": "value"
                                        }
                                    ]
                                }
                            }
                        ]
                    },
                    "resource_type": "inventory.CloudService",
                    "extend_data": {
                        "label": "Storage"
                    }
                }
            }
        ]
    },
    "schedule": {
        "hours": [
            1
        ]
    },
    "tags": {},
    "domain_id": "domain-58010aa2e451",
    "created_at": "2022-06-13T11:41:35.811Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### list
> **GET** /statistics/v1/schedules
>
> **POST** /statistics/v1/schedules/search


> Gets a list of all Schedules. You can use a query to get a filtered list of Schedules.

| Type | Message |
| :--- | :--- |
| Request | [ScheduleQuery](schedule.md#schedulequery) |
| Response |  [SchedulesInfo](schedule.md#schedulesinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "query": {},
    "domain_id": "domain-58010aa2e451"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "results": [
        {
            "schedule_id": "sch-3da9c9ed2ee2",
            "topic": "daily_cloud_service_summary",
            "state": "ENABLED",
            "options": {
                "aggregate": [
                    {
                        "query": {
                            "query": {
                                "aggregate": [
                                    {
                                        "group": {
                                            "keys": [
                                                {
                                                    "key": "project_id",
                                                    "name": "project_id"
                                                },
                                                {
                                                    "name": "cloud_service_type",
                                                    "key": "cloud_service_type"
                                                },
                                                {
                                                    "name": "cloud_service_group",
                                                    "key": "cloud_service_group"
                                                },
                                                {
                                                    "key": "provider",
                                                    "name": "provider"
                                                }
                                            ],
                                            "fields": [
                                                {
                                                    "operator": "count",
                                                    "name": "value"
                                                }
                                            ]
                                        }
                                    }
                                ],
                                "filter": [
                                    {
                                        "key": "ref_cloud_service_type.is_primary",
                                        "operator": "eq",
                                        "value": true
                                    },
                                    {
                                        "key": "ref_cloud_service_type.labels",
                                        "value": "Server",
                                        "operator": "eq"
                                    }
                                ]
                            },
                            "resource_type": "inventory.CloudService",
                            "extend_data": {
                                "label": "Server"
                            }
                        }
                    },
                    {
                        "concat": {
                            "query": {
                                "aggregate": [
                                    {
                                        "group": {
                                            "keys": [
                                                {
                                                    "key": "project_id",
                                                    "name": "project_id"
                                                },
                                                {
                                                    "name": "cloud_service_type",
                                                    "key": "cloud_service_type"
                                                },
                                                {
                                                    "name": "cloud_service_group",
                                                    "key": "cloud_service_group"
                                                },
                                                {
                                                    "key": "provider",
                                                    "name": "provider"
                                                }
                                            ],
                                            "fields": [
                                                {
                                                    "operator": "count",
                                                    "name": "value"
                                                }
                                            ]
                                        }
                                    }
                                ],
                                "filter": [
                                    {
                                        "operator": "eq",
                                        "key": "ref_cloud_service_type.is_primary",
                                        "value": true
                                    },
                                    {
                                        "key": "ref_cloud_service_type.labels",
                                        "operator": "eq",
                                        "value": "Database"
                                    }
                                ]
                            },
                            "resource_type": "inventory.CloudService",
                            "extend_data": {
                                "label": "Database"
                            }
                        }
                    },
                    {
                        "concat": {
                            "query": {
                                "aggregate": [
                                    {
                                        "group": {
                                            "keys": [
                                                {
                                                    "key": "project_id",
                                                    "name": "project_id"
                                                },
                                                {
                                                    "name": "cloud_service_type",
                                                    "key": "cloud_service_type"
                                                },
                                                {
                                                    "name": "cloud_service_group",
                                                    "key": "cloud_service_group"
                                                },
                                                {
                                                    "key": "provider",
                                                    "name": "provider"
                                                }
                                            ],
                                            "fields": [
                                                {
                                                    "name": "value",
                                                    "operator": "count"
                                                }
                                            ]
                                        }
                                    }
                                ],
                                "filter": [
                                    {
                                        "key": "ref_cloud_service_type.is_primary",
                                        "operator": "eq",
                                        "value": true
                                    },
                                    {
                                        "operator": "eq",
                                        "value": "Container",
                                        "key": "ref_cloud_service_type.labels"
                                    }
                                ]
                            },
                            "resource_type": "inventory.CloudService",
                            "extend_data": {
                                "label": "Container"
                            }
                        }
                    },
                    {
                        "concat": {
                            "query": {
                                "filter": [
                                    {
                                        "key": "ref_cloud_service_type.is_primary",
                                        "value": true,
                                        "operator": "eq"
                                    },
                                    {
                                        "key": "ref_cloud_service_type.labels",
                                        "operator": "eq",
                                        "value": "Networking"
                                    }
                                ],
                                "aggregate": [
                                    {
                                        "group": {
                                            "keys": [
                                                {
                                                    "key": "project_id",
                                                    "name": "project_id"
                                                },
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
                                                    "name": "value",
                                                    "operator": "count"
                                                }
                                            ]
                                        }
                                    }
                                ]
                            },
                            "extend_data": {
                                "label": "Networking"
                            },
                            "resource_type": "inventory.CloudService"
                        }
                    },
                    {
                        "concat": {
                            "extend_data": {
                                "label": "Security"
                            },
                            "query": {
                                "filter": [
                                    {
                                        "key": "ref_cloud_service_type.is_primary",
                                        "value": true,
                                        "operator": "eq"
                                    },
                                    {
                                        "key": "ref_cloud_service_type.labels",
                                        "value": "Security",
                                        "operator": "eq"
                                    }
                                ],
                                "aggregate": [
                                    {
                                        "group": {
                                            "keys": [
                                                {
                                                    "name": "project_id",
                                                    "key": "project_id"
                                                },
                                                {
                                                    "name": "cloud_service_type",
                                                    "key": "cloud_service_type"
                                                },
                                                {
                                                    "name": "cloud_service_group",
                                                    "key": "cloud_service_group"
                                                },
                                                {
                                                    "name": "provider",
                                                    "key": "provider"
                                                }
                                            ],
                                            "fields": [
                                                {
                                                    "operator": "count",
                                                    "name": "value"
                                                }
                                            ]
                                        }
                                    }
                                ]
                            },
                            "resource_type": "inventory.CloudService"
                        }
                    },
                    {
                        "concat": {
                            "resource_type": "inventory.CloudService",
                            "query": {
                                "filter": [
                                    {
                                        "value": true,
                                        "operator": "eq",
                                        "key": "ref_cloud_service_type.is_primary"
                                    },
                                    {
                                        "key": "ref_cloud_service_type.labels",
                                        "operator": "eq",
                                        "value": "Analytics"
                                    }
                                ],
                                "aggregate": [
                                    {
                                        "group": {
                                            "keys": [
                                                {
                                                    "name": "project_id",
                                                    "key": "project_id"
                                                },
                                                {
                                                    "name": "cloud_service_type",
                                                    "key": "cloud_service_type"
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
                                                    "name": "value",
                                                    "operator": "count"
                                                }
                                            ]
                                        }
                                    }
                                ]
                            },
                            "extend_data": {
                                "label": "Analytics"
                            }
                        }
                    },
                    {
                        "concat": {
                            "resource_type": "inventory.CloudService",
                            "query": {
                                "aggregate": [
                                    {
                                        "group": {
                                            "fields": [
                                                {
                                                    "name": "value",
                                                    "operator": "count"
                                                }
                                            ],
                                            "keys": [
                                                {
                                                    "name": "project_id",
                                                    "key": "project_id"
                                                },
                                                {
                                                    "key": "cloud_service_type",
                                                    "name": "cloud_service_type"
                                                },
                                                {
                                                    "key": "cloud_service_group",
                                                    "name": "cloud_service_group"
                                                },
                                                {
                                                    "name": "provider",
                                                    "key": "provider"
                                                }
                                            ]
                                        }
                                    }
                                ],
                                "filter": [
                                    {
                                        "value": true,
                                        "operator": "eq",
                                        "key": "ref_cloud_service_type.is_primary"
                                    }
                                ]
                            },
                            "extend_data": {
                                "label": "All"
                            }
                        }
                    },
                    {
                        "concat": {
                            "resource_type": "inventory.CloudService",
                            "extend_data": {
                                "label": "Storage"
                            },
                            "query": {
                                "filter": [
                                    {
                                        "key": "ref_cloud_service_type.is_major",
                                        "operator": "eq",
                                        "value": true
                                    },
                                    {
                                        "key": "ref_cloud_service_type.labels",
                                        "operator": "eq",
                                        "value": "Storage"
                                    }
                                ],
                                "aggregate": [
                                    {
                                        "group": {
                                            "keys": [
                                                {
                                                    "name": "project_id",
                                                    "key": "project_id"
                                                },
                                                {
                                                    "key": "cloud_service_type",
                                                    "name": "cloud_service_type"
                                                },
                                                {
                                                    "name": "cloud_service_group",
                                                    "key": "cloud_service_group"
                                                },
                                                {
                                                    "key": "provider",
                                                    "name": "provider"
                                                }
                                            ],
                                            "fields": [
                                                {
                                                    "name": "value",
                                                    "operator": "sum",
                                                    "key": "data.size"
                                                }
                                            ]
                                        }
                                    }
                                ]
                            }
                        }
                    }
                ]
            },
            "schedule": {
                "hours": [
                    1
                ]
            },
            "tags": {},
            "domain_id": "domain-58010aa2e451",
            "created_at": "2022-06-13T11:41:35.811Z"
        }
    ],
    "total_count": 1
}
```
{% endtab %}
{% endtabs %}
 
 

 
### stat
> **POST** /statistics/v1/schedules/stat
>


| Type | Message |
| :--- | :--- |
| Request | [ScheduleStatQuery](schedule.md#schedulestatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### AddScheduleRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| topic |string|✔| |
| options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✔| |
| schedule |[Scheduled](schedule.md#scheduled)|✔| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| user_id |string|✔| |
| domain_id |string|✔| |

### GetScheduleRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| schedule_id |string|✔| |
| domain_id |string|✔| |
| only |list of string|✘| |

### QueryOption
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| aggregate |[StatAggregate](schedule.md#stataggregate)|✔| |
| page |[StatPage](schedule.md#statpage)|✘| |

### ScheduleInfo
<table>
  <thead>
    <tr>
      <th style="text-align:left; width:100px;">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left; width:100px;">schedule_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">topic</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">options</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">schedule</td>
      <td style="text-align:left"><a href="schedule.md#scheduled">Scheduled</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">created_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">last_scheduled_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### ScheduleQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|✘| |
| schedule_id |string|✘| |
| topic |string|✘| |
| state |string|✘| |
| resource_type |string|✘| |
| domain_id |string|✔| |

### ScheduleRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| schedule_id |string|✔| |
| domain_id |string|✔| |

### ScheduleStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✔| |
| domain_id |string|✔| |

### Scheduled
| Field | Type |  Description |
| :--- | :--- | :--- |
| cron |string | |
| interval |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |
| minutes |[list of int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |
| hours |[list of int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### SchedulesInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of ScheduleInfo](schedule.md#scheduleinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### UpdateScheduleRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| schedule_id |string|✔| |
| schedule |[Scheduled](schedule.md#scheduled)|✘| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| storage_id |string|✔| |
| domain_id |string|✔| |
