1. Repo Name:
Cellz

2. GitHub Link:
https://github.com/HaseebKahn365/cellz

3. Timeline & Commitment:
August 2023 – August 2023 (Based on commit dates from August 22, 2023 to August 30, 2023) pubspec.yaml:1-5

4. Project Overview:
Cellz is a Flutter-based implementation of the classic "Dots and Boxes" game where players take turns drawing lines between adjacent dots on a grid. When a player completes a square by drawing the fourth line around it, they earn a point and get another turn. The player with the most completed squares when all possible lines have been drawn wins the game.

The target audience is casual gamers looking for a strategic turn-based game that can be played on mobile devices.

The core goals the app solves include providing an interactive digital version of the traditional pen-and-paper game with score tracking, visual feedback, and potential online play capabilities through Firebase integration. main.dart:13-21

5. Core Functionality:
Screens/pages and flow:
The app has a main game screen with a customizable grid of dots where players can draw lines by panning from one dot to another. The UI includes visual feedback for line drawing and square completion.

Business logic layers:
Game Canvas: Central controller for game initialization and state tracking
Game Entities: Points, Lines, Squares, and GamePlayers classes to represent game state
Game Logic: Functions for creating lines and checking square completion
Communication between modules:
The game uses a centralized approach where the main game controller (GameCanvas) interacts with game entities through direct method calls. User interactions are captured through gesture detection and processed by the game logic.

Real-time or offline behavior:
The game appears to be primarily designed for offline play, but includes Firebase integration for potential online capabilities.

User data handling:
Firebase Authentication and Firebase Database are integrated for user management and data persistence.

Error, state, navigation, and animations management:
State Management: Uses Provider package for state management
Animations: Utilizes flutter_animate package for UI animations like line drawing and point selection
Error Handling: Basic exception handling for invalid line creation create_line_checkSq.dart:11-44 pubspec.yaml:38-44
6. Key Features:
Customizable Game Grid
The game allows for different grid sizes defined by x and y points, making it adaptable to different screen sizes and difficulty levels. main.dart:14-18

Interactive Line Drawing
Players can draw lines by panning from one point to another. The game validates the line creation based on the direction and distance of the pan gesture. create_line_checkSq.dart:169-196

Square Completion Detection
The game automatically detects when a player completes a square and awards points accordingly. create_line_checkSq.dart:48-67

Visual Feedback
Animated UI elements provide visual feedback for line drawing and square completion, enhancing the user experience. main.dart:35-45

Score Tracking
The game keeps track of each player's score based on the number of squares they complete. create_line_checkSq.dart:156-162

7. Flutter/Dart Skills Demonstrated:
State Management
Uses Provider (^6.0.5) for state management, allowing for efficient updates to the UI when the game state changes. pubspec.yaml:38

Async programming & Future/Stream use
Implements Future-based delayed animations for visual feedback. main.dart:39-44

Custom Widgets
Develops custom widgets for game elements like points and lines, making the code more modular and reusable. main.dart:94-96

Gesture Detection
Implements complex gesture detection for line drawing, including pan start, update, and end events. main.dart:58-93

8. Architecture & Design Decisions:
Architecture Pattern
The project appears to follow a component-based architecture with clear separation between game logic, UI components, and data structures.

Folder Structure and Separation of Concerns
game_classes: Contains core game logic classes
global_functions: Houses utility functions for game mechanics
game_ui_components: Includes UI-specific components for rendering game elements
lists_of_objects: Manages global lists of game entities
Testability and Modularity
The separation of game logic from UI components makes the code more testable. The project includes Flutter's testing framework for potential unit and widget testing. pubspec.yaml:47-49

9. Third-Party Tools & Packages:
Firebase Core, Auth, and Database
Used for backend services, user authentication, and data persistence. pubspec.yaml:39-41

Provider
Implemented for state management across the application. pubspec.yaml:38

Flutter Animate
Utilized for creating smooth animations for UI elements like line drawing and point selection. pubspec.yaml:44

Flutter Dialogs and Fluttertoast
Employed for user notifications and interactive dialog boxes. pubspec.yaml:42-43

10. Advanced Concepts:
Firebase Integration
The app integrates Firebase Authentication and Realtime Database, potentially allowing for user accounts and online play capabilities. pubspec.yaml:39-41

Custom Animation System
Implements a custom animation system for game elements, enhancing the visual experience. main.dart:35-45

11. Biggest Technical Challenges & Solutions:
Line Drawing Validation
Challenge: Accurately detecting and validating line creation based on user gestures.
Solution: Implemented an offset analyzer function that calculates the difference between start and end points of a pan gesture and validates line creation based on direction and distance thresholds. create_line_checkSq.dart:169-196

Square Completion Detection
Challenge: Detecting when a player completes a square by drawing the fourth line.
Solution: Created a system to check if a newly drawn line completes a square by verifying the existence of three other lines that form a closed shape. create_line_checkSq.dart:48-67

UI Animation Coordination
Challenge: Coordinating animations for line drawing and point selection.
Solution: Used the flutter_animate package and Future-based delayed animations to create smooth visual transitions. main.dart:35-45

12. My Role:
Based on the git blame information, it appears that HaseebKahn365 was the sole contributor to this project, implementing all aspects of the game including:

Core game logic and data structures
UI components and animations
Firebase integration
Gesture detection and user interaction
The project was developed over a period of about 8 days in August 2023, with multiple commits showing the evolution of the game's features and functionality. pubspec.yaml:1

Notes
This template was filled out based on the available code snippets and wiki information from the Cellz repository. The project appears to be a Flutter implementation of the classic Dots and Boxes game with Firebase integration. The development timeline was inferred from commit dates in the provided code snippets. Some sections might be incomplete due to limited access to the full codebase.