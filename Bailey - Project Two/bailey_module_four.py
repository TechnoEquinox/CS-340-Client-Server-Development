#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  2 01:22:14 2025

@author: connorbailey_snhu
"""
import os
from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter:
    """ CRUD operations for the Animal collection in MongoDB """
    
    def __init__(self, user, password, db='AAC', col='animals'):
        """ Initialize the connection to MongoDB """
        # Get the DB environment variables
        try:
            host = os.environ.get('MONGO_HOST')
            port = os.environ.get('MONGO_PORT')
        except Exception as error:
            raise EnvironmentError("Missing one or more MongoDB environment variables.")
        
        # Connect to MongoDB
        try:
            print(f"Connecting with user={user}, password={password}, host={host}, port={port}, db={db}")
            # self.client = MongoClient(f"mongodb://{user}:{password}@{host}:{port}/{db}")
            self.client = MongoClient(f"mongodb://{user}:{password}@{host}:{port}/?authSource={db}")
            self.database = self.client[db]
            self.collection = self.database[col]
        
        except Exception as error:
            raise ConnectionError(f"Unable to connect to the MongoDB database:\n{error}")
    
    def create(self, data):
        """ 
        Create a document and insert it into the collection.
        
        Parameters:
            - data (dict): New document to be inserted into the db
            
        Returns:
            - None
        """
        # Validate the data
        if data is not None and isinstance(data, dict):
            try:
                # Insert the document
                self.collection.insert_one(data)
            except Exception as error:
                print(f"An error occured when attempting to insert the document into {self.database}:\n{error}")
        else:
            raise ValueError(f"An error occured when attempting to insert the document into {self.database}:\nData must be a non-empty dictionary.")
    
    def read(self, query):
        """ 
        Find a document and return a list of results.
        
        Parameters: 
            - query (dict): The filter for selecting documents to read
        
        Returns:
            list: Results from the query
        """
        try:
            results = list(self.collection.find(query))
            return results
        except Exception as error:
            print(f"An error occured when attempting to read a document from {self.database}:\n{error}")
            return []
    
    def update(self, query, new_values):
        """
        Update documents in the collection matching the query with new values.
        
        Parameters:
            - query (dict): The filter for selecting documents to update
            - new_values (dict): The values to update in the selected document
            
        Returns:
            int: The number of documents modified
        """
        try:
            result = self.collection.update_many(query, {"$set": new_values})
            return result.modified_count
        except Exception as error:
            print(f"An error occurred while attempting to update documents in {self.database}:\n{error}")
            return 0
        
    
    def delete(self, query):
        """
        Delete documents from the collection matching the provided query.
        
        Parameters:
            - query (dict): The filter for selecting documents to delete
            
        Returns:
            - int: Number of documents deleted from the db
        """
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except Exception as error:
            print(f"An error occurred while attempting to delete the documents from {self.database}:\n{error}")
            return 0
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
