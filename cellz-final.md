# Cellz Final

## GitHub Link:
(this is a private repo because this is currently in production)

## Timeline & Commitment:
**Start Date:** July 2024  
**End Date:** May 2025  

---

## Project Overview:
Cellz Final is a feature-rich puzzle game designed to provide an engaging and challenging experience for players of all ages. The game revolves around completing levels by achieving specific goals, such as collecting stars or solving puzzles within a time limit. It includes a variety of levels, animations, and sound effects to enhance the user experience.

The target audience includes casual gamers and puzzle enthusiasts. The app aims to provide entertainment while improving problem-solving skills and strategic thinking. Core goals include seamless gameplay, intuitive UI, and a rewarding progression system.

---

## Core Functionality:
### Internal Workflow:
- **Screens/Pages:**  
  The app includes multiple screens such as the Home Screen, Levels Journey, Game Play Screen, Profile Settings, and Friends Interaction.
  
- **Business Logic Layers:**  
  The app uses `Provider` for state management, ensuring a clean separation between UI and business logic. Game states, user data, and level progression are managed efficiently.

- **Communication Between Modules:**  
  Modules communicate via `Provider` and `ChangeNotifier`, ensuring reactive updates across the app.

- **Real-Time or Offline Behavior:**  
  The app supports offline gameplay with local data storage using `sqflite`. Online features like leaderboards and friend interactions are synced with Firebase.

- **User Data Handling:**  
  CRUD operations are implemented for user profiles, game progress, and settings. Data is synced with Firebase for online users and stored locally for offline users.

- **Error, State, Navigation, and Animations:**  
  Errors are handled gracefully with fallback UI. Navigation is managed using `GoRouter`, and animations are implemented using `flutter_animate` for smooth transitions.

---

## Key Features:
1. **Levels Journey:**  
   A timeline-based level progression system with visual indicators for completed, current, and locked levels.

2. **Custom Levels:**  
   Players can create and play custom levels, stored locally or shared with friends.

3. **Audio Integration:**  
   Background music and sound effects enhance the gaming experience. Audio settings are customizable.

4. **Friends Interaction:**  
   Add friends, share progress, and compete on leaderboards.

5. **Offline Support:**  
   Play seamlessly without an internet connection. Data syncs when online.

6. **Haptics and Animations:**  
   Integrated haptic feedback and smooth animations for an immersive experience.

---

## Flutter/Dart Skills Demonstrated:
- **State Management:**  
  Used `Provider` for managing game states, user data, and UI updates.

- **Routing:**  
  Implemented `GoRouter` for dynamic and declarative navigation.

- **Async Programming:**  
  Used `Future` and `Stream` for handling Firebase data sync and real-time updates.

- **Custom Widgets:**  
  Designed reusable widgets like `Grid`, `CircleWidget`, and custom dialogs for modularity.

- **Animations:**  
  Leveraged `flutter_animate` for shimmer effects, transitions, and smooth UI interactions.

---

## Architecture & Design Decisions:
- **Architecture Pattern:**  
  Followed MVVM (Model-View-ViewModel) for clean separation of concerns.

- **Folder Structure:**  
  Organized into `business_logic`, `providers`, `screens`, `widgets`, and `data` folders for modularity and scalability.

- **Testability:**  
  The app is modular and testable, with clear separation between UI and logic.

---

## Third-Party Tools & Packages:
1. **Firebase:**  
   Used for authentication, Firestore database, and cloud storage.

2. **sqflite:**  
   Local database for offline support.

3. **flutter_animate:**  
   For animations like shimmer effects and transitions.

4. **audioplayers:**  
   For background music and sound effects.

5. **timeline_tile:**  
   For the Levels Journey screen.

6. **carousel_slider:**  
   For showcasing levels and features.

---

## Advanced Concepts:
- **Firebase Integration:**  
  Implemented Firebase Authentication, Firestore, and Cloud Storage for real-time data sync.

- **Offline Support:**  
  Ensured seamless gameplay with local storage and sync mechanisms.

- **Haptics and Animations:**  
  Added haptic feedback and smooth animations for an immersive experience.

---

## Biggest Technical Challenges & My Solutions:
1. **Performance Issues with Audio:**  
   Resolved by optimizing audio playback and disabling unnecessary audio streams.

2. **Navigation Bugs:**  
   Fixed by migrating to `GoRouter` for a declarative and robust navigation system.

3. **Data Sync Conflicts:**  
   Implemented conflict resolution strategies for Firebase and local data sync.

---

## My Role:
I was the sole developer and designer of this project. I implemented all features, designed the UI/UX, and managed the integration of third-party tools. I also handled debugging, testing, and deployment to ensure a smooth user experience.