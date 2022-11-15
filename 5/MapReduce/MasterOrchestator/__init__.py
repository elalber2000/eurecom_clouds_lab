# This function is not intended to be invoked directly. Instead it will be
# triggered by an HTTP starter function.
# Before running this sample, please:
# - create a Durable activity function (default name is "Hello")
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import json

import azure.functions as func
import azure.durable_functions as df

import os, uuid
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient


def orchestrator_function(context: df.DurableOrchestrationContext):
    #Get the text from the blob
    TEXT = shuffleTask = yield context.call_activity('GetInputDataFn', "")
    files = TEXT.split('\n')

    #Call the mappers
    mapTasks = []
    for file in files:
        mapTasks.append(context.call_activity("Mapper", file))
    
    mapTasks = yield context.task_all(mapTasks)
    
    
    #Call the shuffler
    shuffleTask = yield context.call_activity('Shuffler', mapTasks)

    
    #Call the reducers
    reduceTasks = []
    for file in shuffleTask:
        reduceTasks.append(context.call_activity("Reducer", file))

    reduceTasks = yield context.task_all(reduceTasks)

    
    return reduceTasks

main = df.Orchestrator.create(orchestrator_function)