# Chicago Lobbyist Database App

## Overview

This Python application provides an interface to analyze lobbyist data stored in an SQLite database. The app allows users to search for lobbyists, view details about individual lobbyists, and retrieve various statistics and records related to lobbyists, clients, and employers.

The application consists of three main components:
1. **`main.py`**: Provides a command-line interface for interacting with the database.
2. **`datatier.py`**: Executes SQL queries against the database and returns results.
3. **`objecttier.py`**: Constructs and manages objects representing lobbyists and their details based on data retrieved from the database.

## Features

- Search for lobbyists by name (supports SQL wildcards).
- View detailed information about specific lobbyists, including address, contact details, and employers.
- Retrieve the top N lobbyists based on total compensation in a given year.
- Add new registration years for lobbyists.
- Update or set the salutation of a lobbyist.

## Commands

The application supports the following commands:
- **Command 1**: Search for lobbyists by name.
- **Command 2**: View detailed information for a lobbyist by ID.
- **Command 3**: Retrieve the top N lobbyists based on total compensation in a given year.
- **Command 4**: Register a new year for an existing lobbyist.
- **Command 5**: Set or update a lobbyist’s salutation.

## Prerequisites

Before running the application, ensure that you have the following installed:
- **Python 3.x**
- **SQLite** (for handling the database)
- **Required Python Libraries**: 
    - `sqlite3`

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/Chicago-Lobbyist-Database-App.git
   cd Chicago-Lobbyist-Database-App
