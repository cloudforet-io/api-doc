---
title: "Schedule"
linkTitle: "Schedule"
weight: 3
bookFlatSection: true
---
# [Schedule](#Schedule)
A Schedule is a time schedule of when a User will use a query.


>  **Package : spaceone.api.statistics.v1**

<br>
<br>

## Schedule





**Schedule Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**add**](./Schedule#add) | [AddScheduleRequest](Schedule#addschedulerequest) | [ScheduleInfo](Schedule#scheduleinfo) |
| [**update**](./Schedule#update) | [UpdateScheduleRequest](Schedule#updateschedulerequest) | [ScheduleInfo](Schedule#scheduleinfo) |
| [**enable**](./Schedule#enable) | [ScheduleRequest](Schedule#schedulerequest) | [ScheduleInfo](Schedule#scheduleinfo) |
| [**disable**](./Schedule#disable) | [ScheduleRequest](Schedule#schedulerequest) | [ScheduleInfo](Schedule#scheduleinfo) |
| [**delete**](./Schedule#delete) | [ScheduleRequest](Schedule#schedulerequest) | [Empty](Schedule#empty) |
| [**get**](./Schedule#get) | [GetScheduleRequest](Schedule#getschedulerequest) | [ScheduleInfo](Schedule#scheduleinfo) |
| [**list**](./Schedule#list) | [ScheduleQuery](Schedule#schedulequery) | [SchedulesInfo](Schedule#schedulesinfo) |
| [**stat**](./Schedule#stat) | [ScheduleStatQuery](Schedule#schedulestatquery) | [Struct](Schedule#struct) |



    
<br>

### add

Adds a new Schedule. When creating, `topic` and queries to be used should be specified. The time interval of the Schedule should be also specified to run queries repeatedly. The run set by Schedule starts every hour on the hour.



> **POST** /statistics/v1/schedule/add
>





 {{< tabs " add " >}}

 {{< tab "Request Example" >}}



[AddScheduleRequest](./Schedule#addschedulerequest)

* **topic** (string)   `Required` 


* **options** (Struct)   `Required` 


* **schedule** (Scheduled)   `Required` 


* **tags** (Struct)  





{{< highlight json >}}
{
   "topic": "daily_cloud_service_summary_test",
   "options": {"aggregate": [{"query": {
       "extend_data": {"label": "Server"}, "query": {
           "filter": [{"key": "ref_cloud_service_type.is_primary", "value": true, "operator": "eq"},
                      {"value": "Server", "operator": "eq", "key": "ref_cloud_service_type.labels"}],
           "aggregate": [{"group": {
               "fields": [
                   {
                       "name": "value",
                       "operator": "count"}],
               "keys": [
                   {
                       "name": "project_id",
                       "key": "project_id"},
                   {
                       "key": "cloud_service_type",
                       "name": "cloud_service_type"},
                   {
                       "key": "cloud_service_group",
                       "name": "cloud_service_group"},
                   {
                       "key": "provider",
                       "name": "provider"}]}}]},
       "resource_type": "inventory.CloudService"}}, {"concat": {"resource_type": "inventory.CloudService", "query": {
       "aggregate": [{"group": {"keys": [{"key": "project_id", "name": "project_id"},
                                         {"name": "cloud_service_type", "key": "cloud_service_type"},
                                         {"key": "cloud_service_group", "name": "cloud_service_group"},
                                         {"key": "provider", "name": "provider"}],
                                "fields": [{"name": "value", "operator": "count"}]}}],
       "filter": [{"value": true, "operator": "eq", "key": "ref_cloud_service_type.is_primary"},
                  {"value": "Database", "operator": "eq", "key": "ref_cloud_service_type.labels"}]},
                                                                "extend_data": {"label": "Database"}}}, {"concat": {
       "resource_type": "inventory.CloudService", "extend_data": {"label": "Container"}, "query": {
           "filter": [{"value": true, "key": "ref_cloud_service_type.is_primary", "operator": "eq"},
                      {"key": "ref_cloud_service_type.labels", "value": "Container", "operator": "eq"}],
           "aggregate": [{
               "group": {
                   "fields": [
                       {
                           "name": "value",
                           "operator": "count"}],
                   "keys": [
                       {
                           "key": "project_id",
                           "name": "project_id"},
                       {
                           "name": "cloud_service_type",
                           "key": "cloud_service_type"},
                       {
                           "name": "cloud_service_group",
                           "key": "cloud_service_group"},
                       {
                           "key": "provider",
                           "name": "provider"}]}}]}}},
       {"concat": {
           "extend_data": {"label": "Networking"},
           "query": {"aggregate": [{"group": {
               "keys": [{"name": "project_id",
                         "key": "project_id"}, {
                            "key": "cloud_service_type",
                            "name": "cloud_service_type"},
                        {
                            "key": "cloud_service_group",
                            "name": "cloud_service_group"},
                        {"key": "provider",
                         "name": "provider"}],
               "fields": [{"name": "value",
                           "operator": "count"}]}}],
               "filter": [{
                   "key": "ref_cloud_service_type.is_primary",
                   "operator": "eq",
                   "value": true},
                   {
                       "key": "ref_cloud_service_type.labels",
                       "value": "Networking",
                       "operator": "eq"}]},
           "resource_type": "inventory.CloudService"}},
       {"concat": {
           "resource_type": "inventory.CloudService",
           "query": {"filter": [{
               "key": "ref_cloud_service_type.is_primary",
               "value": true,
               "operator": "eq"},
               {"operator": "eq",
                "value": "Security",
                "key": "ref_cloud_service_type.labels"}],
               "aggregate": [{"group": {
                   "keys": [
                       {"key": "project_id",
                        "name": "project_id"},
                       {
                           "key": "cloud_service_type",
                           "name": "cloud_service_type"},
                       {
                           "name": "cloud_service_group",
                           "key": "cloud_service_group"},
                       {"key": "provider",
                        "name": "provider"}],
                   "fields": [
                       {"name": "value",
                        "operator": "count"}]}}]},
           "extend_data": {"label": "Security"}}},
       {"concat": {
           "resource_type": "inventory.CloudService",
           "extend_data": {"label": "Analytics"},
           "query": {"filter": [{"value": true,
                                 "key": "ref_cloud_service_type.is_primary",
                                 "operator": "eq"},
                                {"operator": "eq",
                                 "value": "Analytics",
                                 "key": "ref_cloud_service_type.labels"}],
                     "aggregate": [{"group": {
                         "fields": [
                             {"operator": "count",
                              "name": "value"}],
                         "keys": [
                             {"name": "project_id",
                              "key": "project_id"},
                             {
                                 "key": "cloud_service_type",
                                 "name": "cloud_service_type"},
                             {
                                 "key": "cloud_service_group",
                                 "name": "cloud_service_group"},
                             {"key": "provider",
                              "name": "provider"}]}}]}}},
       {"concat": {
           "resource_type": "inventory.CloudService",
           "extend_data": {"label": "All"},
           "query": {"aggregate": [{"group": {
               "keys": [{"name": "project_id",
                         "key": "project_id"}, {
                            "name": "cloud_service_type",
                            "key": "cloud_service_type"},
                        {
                            "name": "cloud_service_group",
                            "key": "cloud_service_group"},
                        {"key": "provider",
                         "name": "provider"}],
               "fields": [{"operator": "count",
                           "name": "value"}]}}],
               "filter": [{
                   "key": "ref_cloud_service_type.is_primary",
                   "operator": "eq",
                   "value": true}]}}},
       {"concat": {"query": {"filter": [
           {"value": true, "operator": "eq",
            "key": "ref_cloud_service_type.is_major"},
           {"value": "Storage", "operator": "eq",
            "key": "ref_cloud_service_type.labels"}],
           "aggregate": [{
               "group": {
                   "fields": [
                       {
                           "name": "value",
                           "key": "data.size",
                           "operator": "sum"}],
                   "keys": [
                       {
                           "name": "project_id",
                           "key": "project_id"},
                       {
                           "name": "cloud_service_type",
                           "key": "cloud_service_type"},
                       {
                           "key": "cloud_service_group",
                           "name": "cloud_service_group"},
                       {
                           "key": "provider",
                           "name": "provider"}]}}]},
           "resource_type": "inventory.CloudService",
           "extend_data": {
               "label": "Storage"}
       }}]},
   "schedule": {"hours": [1]},
   "tags": {},
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[ScheduleInfo](#SCHEDULEINFO)
* **schedule_id** (string)   `Required` 

* **topic** (string)   `Required` 

* **state** (State)   `Required` 

* **options** (Struct)   `Required` 

* **schedule** (Scheduled)   `Required` 

* **tags** (Struct)   `Required` 

* **domain_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **last_scheduled_at** (string)   `Required` 



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### update

Updates a specific Schedule. You can make changes in Schedule settings, including time intervals.



> **POST** /statistics/schedule/update
>





 {{< tabs " update " >}}

 {{< tab "Request Example" >}}



[UpdateScheduleRequest](./Schedule#updateschedulerequest)

* **schedule_id** (string)   `Required` 


* **schedule** (Scheduled)  


* **tags** (Struct)  





{{< highlight json >}}
{
   "schedule_id": "sch-65bb6b55d162",
   "schedule": {"hours": [2]},
   "tags": {"a": "b"},
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[ScheduleInfo](#SCHEDULEINFO)
* **schedule_id** (string)   `Required` 

* **topic** (string)   `Required` 

* **state** (State)   `Required` 

* **options** (Struct)   `Required` 

* **schedule** (Scheduled)   `Required` 

* **tags** (Struct)   `Required` 

* **domain_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **last_scheduled_at** (string)   `Required` 



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### enable

Enables a specific Schedule. If a Schedule is enabled, the query usage will be scheduled by the time interval specified.



> **POST** /statistics/v1/schedule/enable
>





 {{< tabs " enable " >}}

 {{< tab "Request Example" >}}



[ScheduleRequest](./Schedule#schedulerequest)

* **schedule_id** (string)   `Required` 





{{< highlight json >}}
{
   "schedule_id": "sch-65bb6b55d162",
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[ScheduleInfo](#SCHEDULEINFO)
* **schedule_id** (string)   `Required` 

* **topic** (string)   `Required` 

* **state** (State)   `Required` 

* **options** (Struct)   `Required` 

* **schedule** (Scheduled)   `Required` 

* **tags** (Struct)   `Required` 

* **domain_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **last_scheduled_at** (string)   `Required` 



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### disable

Disables a specific Schedule. If a Schedule is disabled, the query usage will not be scheduled.



> **POST** /statistics/v1/schedule/disable
>





 {{< tabs " disable " >}}

 {{< tab "Request Example" >}}



[ScheduleRequest](./Schedule#schedulerequest)

* **schedule_id** (string)   `Required` 





{{< highlight json >}}
{
   "schedule_id": "sch-65bb6b55d162",
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[ScheduleInfo](#SCHEDULEINFO)
* **schedule_id** (string)   `Required` 

* **topic** (string)   `Required` 

* **state** (State)   `Required` 

* **options** (Struct)   `Required` 

* **schedule** (Scheduled)   `Required` 

* **tags** (Struct)   `Required` 

* **domain_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **last_scheduled_at** (string)   `Required` 



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### delete

Deletes a specific Schedule. You must specify the `schedule_id` of the Schedule to delete.



> **POST** /statistics/v1/schedule/delete
>





 {{< tabs " delete " >}}

 {{< tab "Request Example" >}}



[ScheduleRequest](./Schedule#schedulerequest)

* **schedule_id** (string)   `Required` 





{{< highlight json >}}
{
   "schedule_id": "sch-65bb6b55d162",
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### get

Gets a specific Schedule. Prints detailed information about the Schedule, including the schedule interval and `state`.



> **POST** /statistics/v1/schedule/get
>





 {{< tabs " get " >}}

 {{< tab "Request Example" >}}



[GetScheduleRequest](./Schedule#getschedulerequest)

* **schedule_id** (string)   `Required` 





{{< highlight json >}}
{
   "schedule_id": "sch-3da9c9ed2ee2",
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[ScheduleInfo](#SCHEDULEINFO)
* **schedule_id** (string)   `Required` 

* **topic** (string)   `Required` 

* **state** (State)   `Required` 

* **options** (Struct)   `Required` 

* **schedule** (Scheduled)   `Required` 

* **tags** (Struct)   `Required` 

* **domain_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **last_scheduled_at** (string)   `Required` 



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### list

Gets a list of all Schedules. You can use a query to get a filtered list of Schedules.



> **POST** /statistics/v1/schedule/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[ScheduleQuery](./Schedule#schedulequery)

* **query** (Query)  


* **schedule_id** (string)  


* **topic** (string)  


* **state** (string)  


* **resource_type** (string)  





{{< highlight json >}}
{
   "query": {},
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[SchedulesInfo](#SCHEDULESINFO)
* **results** (ScheduleInfo)  `Repeated`   `Required` 

* **total_count** (int32)   `Required` 



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### stat





> **POST** /statistics/v1/schedule/stat
>






    


<br>
<br>

## Message



### AddScheduleRequest
* **topic** (string)   `Required` 

    
* **options** (Struct)   `Required` 

    
* **schedule** (Scheduled)   `Required` 

    
* **tags** (Struct)  

    <br>

### GetScheduleRequest
* **schedule_id** (string)   `Required` 

    <br>

### QueryOption
* **aggregate** (StatAggregate)   `Required` 

    
* **page** (StatPage)  

    <br>

### ScheduleInfo
* **schedule_id** (string)   `Required` 

    
* **topic** (string)   `Required` 

    
* **state** (State)   `Required` 

    
* **options** (Struct)   `Required` 

    
* **schedule** (Scheduled)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **last_scheduled_at** (string)   `Required` 

    <br>

### ScheduleQuery
* **query** (Query)  

    
* **schedule_id** (string)  

    
* **topic** (string)  

    
* **state** (string)  

    
* **resource_type** (string)  

    <br>

### ScheduleRequest
* **schedule_id** (string)   `Required` 

    <br>

### ScheduleStatQuery
* **query** (StatisticsQuery)   `Required` 

    <br>

### Scheduled
* **cron** (string)   `Required` 

    
* **interval** (int32)   `Required` 

    
* **minutes** (int32)  `Repeated`    `Required` 

    
* **hours** (int32)  `Repeated`    `Required` 

    <br>

### SchedulesInfo
* **results** (ScheduleInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### UpdateScheduleRequest
* **schedule_id** (string)   `Required` 

    
* **schedule** (Scheduled)  

    
* **tags** (Struct)  

    <br>
