---
title: "Resource"
linkTitle: "Resource"
weight: 3
bookFlatSection: true
---
# [Resource](#Resource)
A Resource is a resource used for analysis on all microservices used in Cloudforet.


>  **Package : spaceone.api.statistics.v1**

<br>
<br>

## Resource





**Resource Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**stat**](./Resource#stat) | [ResourceStatRequest](Resource#resourcestatrequest) | [Struct](./Resource#struct) |



    
<br>

### stat

Enables data preprocessing of different services. Although limited, it is possible to create not only basic queries but also data suitable for users' needs, such as joins between two tables created by the query, handling missing values, and sorting.



> **POST** /statistics/v1/resource/stat
>





 {{< tabs " stat " >}}

 {{< tab "Request Example" >}}



[ResourceStatRequest](./Resource#resourcestatrequest)

* **aggregate** (StatAggregate)  `Required` 


* **domain_id** (string)  `Required` 


* **page** (StatPage) 





{{< highlight json >}}
{
   "aggregate": [
       {"query": {"resource_type": "inventory.CloudServiceType",
                  "query": {
                      "filter": [{"k": "labels", "v": ["Server"], "o": "in"},
                                 {"k": "is_primary", "v": true, "o": "eq"}], "aggregate": [{
                          "group": {
                              "keys": [
                                  {
                                      "key": "cloud_service_type_id",
                                      "name": "cloud_service_type_id"},
                                  {
                                      "key": "name",
                                      "name": "cloud_service_type"},
                                  {
                                      "key": "group",
                                      "name": "cloud_service_group"},
                                  {
                                      "key": "provider",
                                      "name": "provider"},
                                  {
                                      "key": "cloud_service_type_id",
                                      "name": "cloud_service_type_id"}],
                              "fields": [
                                  {
                                      "key": "tags",
                                      "name": "tags",
                                      "operator": "first"},
                                  {
                                      "key": "labels",
                                      "name": "labels",
                                      "operator": "first"}]}}]}}},
       {"join": {"resource_type": "inventory.CloudService", "query": {"filter": [
           {"k": "ref_cloud_service_type.cloud_service_type_id",
            "v": ["cloud-svc-type-58c926b19aca", "cloud-svc-type-c7e5bc38d911",
                  "cloud-svc-type-8dd4d7a13b95", "cloud-svc-type-719e705cb529",
                  "cloud-svc-type-50bd62cf6e0e"], "o": "in"}], "aggregate": [{"group": {
           "keys": [{"key": "cloud_service_type", "name": "cloud_service_type"},
                    {"key": "cloud_service_group", "name": "cloud_service_group"},
                    {"key": "provider", "name": "provider"}],
           "fields": [{"name": "count", "operator": "count"}]}}]},
                 "keys": ["cloud_service_type", "cloud_service_group", "provider"]}},
       {"fill_na": {"data": {"count": 0.0}}}, {"formula": {"query": "count > 0"}},
       {"sort": {"key": "count", "desc": true}}],
   "domain_id": "domain-58010aa2e451"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    


<br>
<br>

## Message



### ResourceStatRequest
* **aggregate** (StatAggregate)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **page** (StatPage) 

    <br>

### SortKey
* **key** (string)  `Required` 

    
* **desc** (bool)  `Required` 

    <br>

### StatAggregate
* **query** (StatAggregateQuery)  `Required` 

    
* **join** (StatAggregateJoin)  `Required` 

    
* **concat** (StatAggregateConcat)  `Required` 

    
* **sort** (StatAggregateSort)  `Required` 

    
* **formula** (StatAggregateFormula)  `Required` 

    
* **fill_na** (StatAggregateFillNA)  `Required` 

    <br>

### StatAggregateConcat
* **resource_type** (string)  `Required` 

    
* **query** (StatisticsQuery)  `Required` 

    
* **extend_data** (Struct) 

    <br>

### StatAggregateFillNA
* **data** (Struct)  `Required` 

    <br>

### StatAggregateFormula
* **eval** (string)  `Required` 

    
* **query** (string)  `Required` 

    <br>

### StatAggregateJoin
* **resource_type** (string)  `Required` 

    
* **query** (StatisticsQuery)  `Required` 

    
* **extend_data** (Struct) 

    
* **type** (JoinType) 

    
* **keys** (string) 

    <br>

### StatAggregateQuery
* **resource_type** (string)  `Required` 

    
* **query** (StatisticsQuery)  `Required` 

    
* **extend_data** (Struct) 

    <br>

### StatAggregateSort
* **key** (string) 

    
* **desc** (bool) 

    
* **keys** (SortKey) 

    <br>

### StatPage
* **limit** (uint32)  `Required` 

    
* **start** (uint32) 

    <br>
