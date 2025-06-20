-- Step 1: Create Database
CREATE DATABASE VirtualArtGallery;
GO

USE VirtualArtGallery;
GO

-- Step 2: Create Tables

CREATE TABLE Artist (
    ArtistID INT PRIMARY KEY IDENTITY(1,1),
    Name NVARCHAR(100),
    Biography NVARCHAR(MAX),
    BirthDate DATE,
    Nationality NVARCHAR(50),
    Website NVARCHAR(100),
    ContactInfo NVARCHAR(100)
);

CREATE TABLE Artwork (
    ArtworkID INT PRIMARY KEY IDENTITY(1,1),
    Title NVARCHAR(100),
    Description NVARCHAR(MAX),
    CreationDate DATE,
    Medium NVARCHAR(50),
    ImageURL NVARCHAR(255),
    ArtistID INT FOREIGN KEY REFERENCES Artist(ArtistID)
);

CREATE TABLE AppUser (
    UserID INT PRIMARY KEY IDENTITY(1,1),
    Username NVARCHAR(50),
    Password NVARCHAR(100),
    Email NVARCHAR(100),
    FirstName NVARCHAR(50),
    LastName NVARCHAR(50),
    DOB DATE,
    ProfilePic NVARCHAR(255)
);

CREATE TABLE User_Favorite_Artwork (
    UserID INT,
    ArtworkID INT,
    PRIMARY KEY (UserID, ArtworkID),
    FOREIGN KEY (UserID) REFERENCES AppUser(UserID),
    FOREIGN KEY (ArtworkID) REFERENCES Artwork(ArtworkID)
);

CREATE TABLE Gallery (
    GalleryID INT PRIMARY KEY IDENTITY(1,1),
    Name NVARCHAR(100),
    Description NVARCHAR(MAX),
    Location NVARCHAR(100),
    CuratorID INT FOREIGN KEY REFERENCES Artist(ArtistID),
    OpeningHours NVARCHAR(100)
);

CREATE TABLE Artwork_Gallery (
    ArtworkID INT,
    GalleryID INT,
    PRIMARY KEY (ArtworkID, GalleryID),
    FOREIGN KEY (ArtworkID) REFERENCES Artwork(ArtworkID),
    FOREIGN KEY (GalleryID) REFERENCES Gallery(GalleryID)
);