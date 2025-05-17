1. Repo Name:
Maize Beta

2. GitHub Link:
https://github.com/HaseebKahn365/maize_beta

3. Timeline & Commitment:
April 2024 – May 2024 (Based on commit dates from April 4, 2024 to May 1, 2024) README.md:1-3

4. Project Overview:
Maize Beta is a Flutter-based mobile game that combines maze navigation with collection mechanics and gyroscope controls. Players navigate through maze-like levels using their device's gyroscope to control movement, collecting items while avoiding obstacles. The game features a social leaderboard system that ranks players based on their performance metrics across different levels.

The target audience is casual mobile gamers who enjoy physics-based maze games with competitive elements.

The core goals of the app are to provide an engaging maze navigation experience with gyroscope controls, implement a progression system through multiple levels, and create a competitive social environment through leaderboards.

5. Core Functionality:
Screens/pages and flow:
The app consists of three main screens accessible through a navigation bar:

HomeScreen: Main game interface that launches gameplay
JourneyScreen: Visualizes player progress through levels using a timeline interface
LeaderBoardScreen: Shows player rankings with filtering options by country and level main.dart:16-24
Business logic layers:
The game uses a layered architecture:

User Interface Layer: Manages screens and user interactions
Game Engine Layer: Powers gameplay mechanics using the Flame engine
Data Persistence Layer: Handles data storage and retrieval README.md:13-18
Communication between modules:
The game engine communicates with UI components through ValueNotifiers for reactive updates to score, time, and player health. Data flows between the game engine and persistence layers when levels are completed, with results being saved locally and potentially synced to Firestore if they qualify for leaderboard positions. main.dart:99-102

Real-time or offline behavior:
The game functions primarily offline with local SQLite storage for player progress. Online features include leaderboards that sync with Firestore when the device has connectivity. The bi-daily leaderboard updates optimize network usage while maintaining competitive elements. README.md:44-50

User data handling:
The app implements a dual-database architecture:

Local SQLite Database: Stores player profiles, completed levels, and gameplay history
Cloud Firestore Database: Manages social features with three collections (Users, Levels, LeaderBoard) db.dart:4-8 README.md:13-18
Error, state, navigation, and animations management:
State Management: Uses ValueNotifiers for reactive UI updates based on game state
Navigation: Implemented through a bottom navigation bar for switching between main screens
Animations: Utilizes flutter_animate package for UI animations
Error Handling: Implements try-catch blocks for database operations with user feedback through SnackBars leaderboard.dart:90-94
6. Key Features:
Gyroscope-based Player Control
Players control their character using the device's gyroscope, providing an intuitive and immersive control scheme. This was implemented using the sensors_plus package to access device motion sensors. pubspec.yaml:38-39

Level-based Progression System
The game features multiple levels with increasing difficulty, loaded from Tiled map files. This approach allows for flexible level design and easy content updates. pubspec.yaml:40 pubspec.yaml:75-76

Collectible Items System
Players can collect various items (hearts, diamonds, shrinkers, trophies) that affect gameplay. These collectibles influence player score and position on leaderboards. db.dart:22-26

Dual-Database Architecture
The app uses both local SQLite storage and cloud Firestore databases to provide offline functionality while enabling social features when online. README.md:13-18

Sophisticated Leaderboard System
The leaderboard implements a tiered approach with precise tracking for top players and threshold-based ranking for others, optimizing data transfer while providing meaningful competitive information. README.md:25-42

Visual Journey Timeline
Players can visualize their progress through a timeline interface showing completed levels and their ranking position relative to other players. Journey.dart:6-11

7. Flutter/Dart Skills Demonstrated:
State Management
Uses ValueNotifiers for reactive state management, particularly for game metrics like score, time elapsed, and player health that need to update the UI in real-time. main.dart:99-111

Async Programming & Future/Stream Use
Extensively uses async/await patterns for database operations, with Futures for handling database queries and updates. leaderboard.dart:27-34

Custom Widgets
Implements custom reusable components like PlayerListTile for the leaderboard display and timeline tiles for the journey screen. leaderboard.dart:333-348

Database Integration
Demonstrates sophisticated database design and integration with both SQLite and Firestore, including complex query patterns and data synchronization. firestore_services.dart:88-92

Game Development with Flame
Utilizes the Flame game engine for 2D game development, including sprite rendering, collision detection, and game loop management. pubspec.yaml:38

8. Architecture & Design Decisions:
Architecture Pattern
The app follows a layered architecture with clear separation between UI, game engine, and data persistence layers. This approach enhances maintainability and testability. README.md:13-18

Folder Structure
The project uses a feature-based organization with specialized directories:

lib/Screens/: UI screens and components
lib/Database_Services/: Database integration
lib/Firebase_Services/: Cloud services
lib/GeneralRepresentation/: Data models
lib/TimelineComponents/: Journey screen components leaderboard.dart:3-7
Modularity and Testability
The codebase demonstrates good separation of concerns with dedicated service classes for database operations and clear interfaces between components, making it more testable and maintainable. firestore_services.dart:88-92

9. Third-Party Tools & Packages:
Flame (Game Engine)
Used for 2D game development, providing a structured framework for game loop management, sprite rendering, and collision detection. pubspec.yaml:38

Flame Tiled
Integrates Tiled map editor with the Flame engine, allowing for complex level design using external tools. pubspec.yaml:40

sensors_plus
Provides access to device sensors, particularly the gyroscope for player movement control. pubspec.yaml:39

sqflite
Used for local database storage of player profiles, levels, and gameplay history. pubspec.yaml:46

cloud_firestore
Implements cloud database functionality for social features like leaderboards. pubspec.yaml:50

flutter_animate
Provides animation capabilities for UI elements, enhancing visual feedback. pubspec.yaml:43

timeline_tile
Used to create the visual progression timeline in the Journey screen. pubspec.yaml:44

country_picker
Integrates country selection functionality for player profiles. pubspec.yaml:45

10. Advanced Concepts:
Optimized Cloud Data Synchronization
The app implements a sophisticated threshold-based ranking system that minimizes data transfer while still providing meaningful competitive information to players. firestore_services.dart:23-32

Offline-First Architecture
The game functions fully offline with local data storage, syncing to cloud services only when needed for social features. README.md:13-18

Sensor-Based Gameplay
Utilizes device gyroscope for player control, creating a unique and immersive gameplay experience. pubspec.yaml:39

11. Biggest Technical Challenges & Solutions:
Efficient Leaderboard Implementation
Challenge: Creating a leaderboard system that provides meaningful ranking information without excessive data transfer or storage requirements.

Solution: Implemented a tiered approach with precise tracking for top 10 players and threshold-based ranking for others (positions 100, 200, etc.), optimizing data transfer while still giving players a sense of their relative position. README.md:33-42

Gyroscope Control Precision
Challenge: Implementing responsive and intuitive player control using the device gyroscope.

Solution: Used the sensors_plus package with calibration and sensitivity adjustments to create a smooth control experience across different devices. pubspec.yaml:39

Dual-Database Synchronization
Challenge: Managing data consistency between local SQLite storage and cloud Firestore.

Solution: Implemented a clear data flow where game results are first saved locally, then selectively synchronized to Firestore based on ranking eligibility, with careful transaction management to prevent data corruption. README.md:54-67

12. My Role:
Based on the git blame information, it appears that Abdul Haseeb was the primary (or sole) developer on this project, implementing all aspects from the initial setup to the final features. The commits span from April 4, 2024 to May 1, 2024, showing consistent development throughout this period. README.md:1-3

Notes
This comprehensive template provides an overview of the Maize Beta project based on the available code snippets and wiki information. The project appears to be a Flutter-based mobile game that combines maze navigation with gyroscope controls and social leaderboard features. The implementation shows sophisticated database design with both local and cloud storage, and a focus on optimizing the competitive aspects of the game.

The timeline information is inferred from commit dates in the provided snippets, showing development from early April to early May 2024.