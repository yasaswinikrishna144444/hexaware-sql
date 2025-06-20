-- Insert Artists
INSERT INTO Artist (Name, Biography, BirthDate, Nationality, Website, ContactInfo)
VALUES
('Vincent van Gogh', 'Dutch post-impressionist painter.', '1853-03-30', 'Dutch', 'http://vangogh.com', 'info@vangogh.com'),
('Leonardo da Vinci', 'Italian polymath.', '1452-04-15', 'Italian', 'http://leonardo.com', 'info@leonardo.com');

-- Insert Artworks
INSERT INTO Artwork (Title, Description, CreationDate, Medium, ImageURL, ArtistID)
VALUES
('Starry Night', 'Famous night sky painting', '1889-06-01', 'Oil on canvas', 'starry.jpg', 1),
('Mona Lisa', 'Portrait of Lisa Gherardini', '1503-10-01', 'Oil on poplar', 'monalisa.jpg', 2);

-- Insert AppUsers
INSERT INTO AppUser (Username, Password, Email, FirstName, LastName, DOB, ProfilePic)
VALUES
('artlover01', 'pass123', 'art01@email.com', 'Anika', 'Sharma', '1995-08-12', 'anika.jpg'),
('galleryfan', 'secure456', 'fan@email.com', 'Rohan', 'Verma', '1989-03-23', 'rohan.png');

-- Insert User Favorites
INSERT INTO User_Favorite_Artwork (UserID, ArtworkID)
VALUES
(1, 1), (2, 2);

-- Insert Galleries
INSERT INTO Gallery (Name, Description, Location, CuratorID, OpeningHours)
VALUES
('Modern Masters', 'Gallery of modern legends', 'New York', 1, '10:00 AM - 6:00 PM'),
('Renaissance Wonders', 'Gallery of renaissance art', 'Florence', 2, '09:00 AM - 5:00 PM');

-- Insert Artwork-Gallery relations
INSERT INTO Artwork_Gallery (ArtworkID, GalleryID)
VALUES
(1, 1), (2, 2);