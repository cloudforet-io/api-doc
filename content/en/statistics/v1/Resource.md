---
title: "Resource"
linkTitle: "Resource"
weight: 3
bookFlatSection: true
---
# [Resource](#Resource)
desc: A Resource is a resource used for analysis on all microservices used in Cloudforet.


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

> **POST** /statistics/v1/resource/stat
>




 {{< tabs " stat " >}}




{{< /tabs >}}

    


<br>
<br>

## Message



### ResourceStatRequest
* **aggregate** (StatAggregate)  `Required` 

  *is_required: true*

    
* **page** (StatPage)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

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

  *is_required: true*

    
* **query** (StatisticsQuery)  `Required` 

  *is_required: true*

    
* **extend_data** (Struct)  `Required` 

  *is_required: false*

    <br>

### StatAggregateFillNA
* **data** (Struct)  `Required` 

  *is_required: true*

    <br>

### StatAggregateFormula
* **eval** (string)  `Required` 

    
* **query** (string)  `Required` 

    <br>

### StatAggregateJoin
* **resource_type** (string)  `Required` 

  *is_required: true*

    
* **query** (StatisticsQuery)  `Required` 

  *is_required: true*

    
* **extend_data** (Struct)  `Required` 

  *is_required: false*

    
* **type** (JoinType)  `Required` 

  *is_required: false*

    
* **keys** (string)  `Required` 

  *is_required: false*

    <br>

### StatAggregateQuery
* **resource_type** (string)  `Required` 

  *is_required: true*

    
* **query** (StatisticsQuery)  `Required` 

  *is_required: true*

    
* **extend_data** (Struct)  `Required` 

  *is_required: false*

    <br>

### StatAggregateSort
* **key** (string)  `Required` 

  *is_required: false*

    
* **desc** (bool)  `Required` 

  *is_required: false*

    
* **keys** (SortKey)  `Required` 

  *is_required: false*

    <br>

### StatPage
* **start** (uint32)  `Required` 

  *is_required: false*

    
* **limit** (uint32)  `Required` 

  *is_required: true*

    <br>
