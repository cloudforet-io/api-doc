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
| [**stat**](./Resource#stat) | [ResourceStatRequest](Resource#resourcestatrequest) | [Struct](Resource#struct) |



    
<br>

### stat

Enables data preprocessing of different services. Although limited, it is possible to create not only basic queries but also data suitable for users' needs, such as joins between two tables created by the query, handling missing values, and sorting.



> **POST** /statistics/v1/resource/stat
>






    


<br>
<br>

## Message



### ResourceStatRequest
* **aggregate** (StatAggregate)  `Repeated`    `Required` 

    
* **page** (StatPage)  

    <br>

### Sort
* **key** (string)   `Required` 

    
* **desc** (bool)   `Required` 

    <br>

### StatAggregate
* **query** (StatAggregateQuery)   `Required` 

    
* **join** (StatAggregateJoin)   `Required` 

    
* **concat** (StatAggregateConcat)   `Required` 

    
* **sort** (StatAggregateSort)   `Required` 

    
* **formula** (StatAggregateFormula)   `Required` 

    
* **fill_na** (StatAggregateFillNA)   `Required` 

    <br>

### StatAggregateConcat
* **resource_type** (string)   `Required` 

    
* **query** (StatisticsQuery)   `Required` 

    
* **extend_data** (Struct)  

    <br>

### StatAggregateFillNA
* **data** (Struct)   `Required` 

    <br>

### StatAggregateFormula
* **eval** (string)   `Required` 

    
* **query** (string)   `Required` 

    <br>

### StatAggregateJoin
* **resource_type** (string)   `Required` 

    
* **query** (StatisticsQuery)   `Required` 

    
* **extend_data** (Struct)  

    
* **type** (JoinType)  

    
* **keys** (string)  `Repeated`   

    <br>

### StatAggregateQuery
* **resource_type** (string)   `Required` 

    
* **query** (StatisticsQuery)   `Required` 

    
* **extend_data** (Struct)  

    <br>

### StatAggregateSort
* **keys** (Sort)  `Repeated`    `Required` 

    <br>

### StatPage
* **limit** (uint32)   `Required` 

    
* **start** (uint32)  

    <br>
