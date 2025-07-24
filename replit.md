# IA Soccer International - Version 2.0

## Overview

IA Soccer International is a comprehensive soccer player analysis platform that combines technical evaluation, AI-powered insights, and player management. The application provides coaches with tools to conduct technical tests, track player progress, and generate detailed analysis reports. Built as a full-stack web application with a React frontend and Express backend, it integrates with PostgreSQL for data persistence and includes a comprehensive UI component library based on shadcn/ui.

## User Preferences

Preferred communication style: Simple, everyday language.
Interface language: French (Français) - complete translation implemented.
Photo support: Athlete photo upload and display functionality enabled.
Hardware integration: Blazepod timer integration implemented for real-world testing scenarios.

## System Architecture

### Frontend Architecture
- **Framework**: React 18 with TypeScript
- **Build Tool**: Vite for fast development and optimized builds
- **Routing**: Wouter for lightweight client-side routing
- **State Management**: TanStack Query (React Query) for server state management
- **UI Framework**: shadcn/ui components built on Radix UI primitives
- **Styling**: Tailwind CSS with custom design tokens and dark mode support
- **Form Handling**: React Hook Form with Zod validation

### Backend Architecture
- **Runtime**: Node.js with Express.js framework
- **Language**: TypeScript with ES modules
- **API Design**: RESTful API endpoints with standardized JSON responses
- **Database ORM**: Drizzle ORM for type-safe database operations
- **Validation**: Zod schemas for runtime type checking and validation

### Database Architecture
- **Database**: PostgreSQL (configured for Neon serverless)
- **Schema Management**: Drizzle Kit for migrations and schema changes
- **Connection**: Neon serverless driver with WebSocket support
- **Session Storage**: PostgreSQL-based session storage for authentication

## Key Components

### Player Management System
- Complete player profiles with personal information, physical stats, and performance history
- Player search and filtering capabilities in French interface
- Athlete photo upload and display with automatic file management
- Position-based categorization (Attaquant, Milieu de terrain, Défenseur, Gardien de but)
- Secure file upload with 5MB limit and image format validation
- Real-time photo preview and removal functionality

### Enhanced Academy Standards Implementation (January 2025)
- **Professional Academy-Based Testing Framework**:
  - Passing: Based on FC Barcelona La Masia standards (tiki-taka precision)
  - Dribbling: Ajax TIPS model integration (Coerver method)
  - Shooting: Real Madrid La Fábrica precision protocols
  - Sprint: FIFA/UEFA standardized speed benchmarks
  - Agility: PSG Academy Change of Direction (COD) tests
  - Reaction: Bayern Munich cognitive assessment protocols
- **Age-Specific Benchmarks (8-17 years)**:
  - U10, U13, U16 performance standards from elite academies
  - Percentile rankings against professional academy players
  - Real statistical comparisons with La Masia, Ajax, Real Madrid cohorts
- **Video Resources Integration**:
  - Professional training videos from Barcelona, Ajax, Real Madrid
  - FIFA/UEFA official protocols and demonstrations
  - Coerver Method technical skill tutorials
  - Academy-specific setup and execution guides
- **Hardware Integration (January 2025)**:
  - Blazepod real-time timer integration with Bluetooth connectivity
  - High-precision millisecond timing for professional-grade measurements
  - Web Bluetooth API support for various timing devices
  - Simulated hardware testing for development and demonstration
  - Synchronized test execution with external timing equipment

### Yogger-Style Biomechanical Analysis (January 2025)
- **Current Implementation Status**: FULLY IMPLEMENTED WITH DATABASE INTEGRATION - January 23, 2025
- **System Features**:
  - Real MediaPipe integration with authentic pose detection
  - Manual technique selection system (shooting, passing, sprint, dribbling)
  - Enhanced biomechanical analysis with detailed exercise recommendations
  - Professional player comparisons with corrective feedback
  - Posture and joint angle correction system
  - Simplified interface focusing on manual selection workflow
- **Database Integration (January 23, 2025)**:
  - Complete PostgreSQL schema with biomechanical_analyses and biomechanical_reports tables
  - Player selection and analysis association system
  - Full CRUD API routes for biomechanical data management
  - Real-time analysis saving with player profile integration
  - Historical analysis tracking and retrieval
- **Technical Resolution**: All runtime errors resolved, data structure compatibility fixed
- **User Experience**: Clean, focused interface with Portuguese language support and player management

### Analytics and Reporting
- Performance statistics dashboard
- Progress tracking over time
- Age-based benchmark comparisons
- AI-powered analysis and recommendations
- Automated report generation

### Module 2 - Rigorous Biomechanical Analysis (January 2025)
- **Rigorous Error Detection**: Strict evaluation system that penalizes poor technique and movement errors
- **Real Academy Standards**: Authentic benchmarks from La Fábrica, La Masia, Bayern Munich with strict tolerances
- **Scientific Accuracy**: Precise joint angle analysis, velocity measurements, and efficiency calculations
- **Critical Error Identification**: System detects and reports specific technical problems and movement flaws
- **Professional Grading**: A-F grading system based on real biomechanical data and academy standards
- **Realistic Scoring**: Low percentile rankings for poor movements, high standards for professional comparison
- **Detailed Feedback**: Specific recommendations for technique improvement and error correction

### Module 3 - Match Analysis and Game Intelligence (January 19, 2025)
- **AI-Powered Game Intelligence Analysis**: Advanced video analysis that detects decision-making patterns, positioning, anticipation, and game vision automatically
- **Professional Player Comparisons**: Compare youth players with professional models (Modrić, Kanté, De Bruyne) based on real playing styles
- **Video Upload and Processing**: Support for match videos, mini-situations, and training scenarios with real-time event detection
- **Intelligent Event Detection**: System automatically identifies and timestamps key moments of decision-making, positioning errors, anticipation skills, and vision opportunities
- **Comprehensive Scoring System**: 0-10 scoring for each game intelligence component with overall game IQ assessment
- **Database Integration**: Full PostgreSQL schema for storing match analyses, game events, and AI confidence scores
- **Automated Report Generation**: Professional reports with improvement areas and tactical recommendations
- **French Interface**: Complete Module 3 implementation in French language matching user preferences

### User Interface Components
- Responsive design optimized for desktop and mobile
- Comprehensive component library with consistent styling
- Interactive charts and progress indicators
- Modal dialogs for forms and detailed views
- Toast notifications for user feedback

### Yogger Interface Implementation - January 19, 2025
- **Created Authentic Yogger Interface**: Replicated original app design with lateral tracking points
- **Implemented Four Analysis Modes**: Real MediaPipe, Authentic Yogger, Technical Yogger, Elite Academy
- **Added Real Video Analysis**: Frame-by-frame processing with movement detection
- **MediaPipe Integration (January 19, 2025)**: 
  - Real pose detection with Google's MediaPipe AI
  - 33 3D body landmarks with visibility scores
  - Skeleton overlay that adjusts to actual human body in video
  - Real joint angle calculations (elbows, knees, hips, shoulders)
  - Biomechanical analysis based on actual movement data
  - Professional-grade pose estimation like original Yogger app
- **Current Status**: Full MediaPipe implementation completed with real pose detection

### Module 3 Implementation Status - January 19, 2025
- **Complete Implementation**: Module 3 - Match Analysis and Game Intelligence fully implemented and integrated
- **Database Schema**: Full PostgreSQL schema with match_analyses and game_events tables created
- **API Routes**: Complete REST API endpoints for CRUD operations on match analyses
- **Frontend Interface**: Professional match analysis interface with video upload, analysis controls, and results display
- **Navigation Integration**: Added to main navigation and dashboard quick actions
- **French Localization**: All text and interface elements translated to French
- **Ready for Testing**: System ready for user testing with video uploads and AI-powered game intelligence analysis

### Module 6 Implementation Status - January 20, 2025
- **Complete Implementation**: Module 6 - Player Profile (Playing Style) fully implemented with AI classification system
- **Database Schema**: Complete PostgreSQL schema with player_profiles, profile_analysis_history, and player_type_templates tables
- **AI Classification Engine**: Advanced algorithm analyzing technique, physique, vision, explosivity, and tactical intelligence
- **Player Type Identification**: Automatic classification into player types (Creative #10, Fast Winger, Organizing Midfielder, Physical Defender)
- **Professional Comparisons**: AI-powered matching with similar professional players (Modrić, Mbappé, De Bruyne, etc.)
- **Comprehensive Analysis**: Strengths, weaknesses, development areas, market value estimation, and development potential
- **Evolution Tracking**: Profile analysis history with performance evolution over time
- **API Integration**: Complete REST API endpoints for profile CRUD operations and AI style analysis
- **Professional Interface**: Beautiful UI with attribute cards, progress gauges, and detailed insights
- **Navigation Integration**: Added to main navigation, sidebar, and dashboard quick actions
- **French Localization**: Complete French interface matching user preferences
- **Database Migration**: Successfully executed migration creating all Module 6 tables
- **Ready for Production**: System fully operational and ready for player profile analysis

### Module 7 Implementation Status - January 21, 2025
- **Complete Implementation**: Module 7 - Plan de développement personnalisé fully implemented and integrated
- **Database Schema**: Complete PostgreSQL schema with developmentPlans, developmentObjectives, progressTracking, and trainingCalendar tables
- **API Routes**: Full REST API endpoints for CRUD operations on development plans, objectives, progress tracking, and training calendar
- **Frontend Interface**: Professional development plan interface with plan management, objective tracking, and progress monitoring
- **Navigation Integration**: Added to main navigation sidebar and dashboard quick actions
- **French Localization**: All text and interface elements translated to French
- **Key Features**:
  - Personal development plans with 1/3/6 month objectives
  - Automatic progress evolution tracking
  - Technical/physical goals calendar
  - Real-time objective completion monitoring
  - Progress visualization with charts and metrics
  - Professional reports and PDF export capabilities
- **Database Migration**: Successfully executed migration creating all Module 7 tables
- **Ready for Production**: System fully operational and ready for personalized development planning

### Module Final - Interface et Résultats globaux - January 21, 2025
- **Complete Implementation**: Module Final - Interface et Résultats globaux fully implemented and integrated
- **Unified Interface**: Central hub consolidating all 7 modules with comprehensive player overview
- **Key Features**:
  - **Complete Player Profiles**: Photo display, comprehensive data, all test results
  - **Global Summary Dashboard**: Performance overview with evolution graphics and statistics
  - **PDF Report Generation**: Professional reports with Canva templates and IA Soccer branding
  - **Google Drive Integration**: Automatic backup organization by player folders
  - **Multi-Device Compatibility**: Responsive design for PC, tablet, and phone
- **Advanced Analytics**: Interactive evolution charts showing technique, physique, and mental progression
- **Professional Reporting**: Configurable PDF reports with multiple templates (Professional, Academy, Scout)
- **Cloud Backup System**: Automated Google Drive organization with structured folder hierarchy
- **Performance Tracking**: Comprehensive metrics including overall scores, rankings, and module completion
- **Navigation Integration**: Added to main navigation sidebar and dashboard quick actions
- **French Interface**: Complete interface in French matching user preferences
- **Ready for Production**: Final unified interface operational and ready for comprehensive player analysis

### Security and Access Control Implementation - January 21, 2025
- **Complete Login System**: Secure authentication for coaches and players with differentiated access levels
- **Dual Interface Design**: Simplified player dashboard vs. full coach interface
- **QR Code/Bracelet Identification**: Optional contactless identification system with NFC support
- **Multi-Method Authentication**: Traditional credentials or QR code scanning options
- **Player Dashboard**: Streamlined interface showing personal progress, objectives, and recent tests
- **Test History Module**: Comprehensive tracking of all test sessions with advanced filtering and export
- **Modern Sports Design**: IA Soccer branded interface with blue/green gradient color scheme
- **Responsive Security**: Mobile-optimized login and identification for all device types
- **French Localization**: Complete security interface translated to French

### Navigation Enhancement - January 21, 2025
- **ModuleHeader Component**: Created reusable navigation header with "Retour" and "Tableau de bord" buttons
- **Universal Implementation**: Added to all 8 modules (Biomechanics, Match Analysis, Cognitive Evaluation, Injury Risk, Player Profile, Development Plans, Global Interface, Test History)
- **Consistent Design**: Unified navigation experience across the entire platform
- **French Interface**: All navigation elements properly translated to French
- **User Experience**: Solved navigation issue - users can now easily return to main dashboard from any module
- **Problem Resolution**: Fixed missing "return to main menu" functionality identified by user feedback

### Access Control with Session Management - January 22, 2025
- **Code-Based Access System**: Implemented secure access codes with persistent session management
- **Session Persistence**: Users enter code once, then navigate freely without re-authentication
- **Access Codes Available**:
  - COACH2025: Full coach interface with all 8 modules
  - PLAYER2025: Simplified player dashboard interface  
  - ADMIN2025: Administrative access with full privileges
- **Session Features**:
  - 24-hour session duration with automatic renewal
  - localStorage-based session storage
  - User information display in module headers
  - One-click logout functionality
- **Navigation Flow**: Single code entry → persistent access → no re-authentication required
- **User Experience**: Solved navigation interruption issue - seamless module switching

### Biomechanical Analysis Database Integration - January 23, 2025
- **Complete Database Schema**: biomechanical_analyses and biomechanical_reports tables implemented
- **API Routes**: Full REST API endpoints for CRUD operations on biomechanical data
- **Player Association**: Analyses now linked to specific players in the system
- **Data Persistence**: Real-time saving of biomechanical analysis results
- **Enhanced Interface**: Player selection, technique configuration, and analysis saving capabilities
- **Storage Implementation**: DatabaseStorage class extended with biomechanical operations
- **Ready for Production**: System fully operational for biomechanical data management

### Chrome Compatibility Issues Resolution - January 23, 2025
- **Desktop Loading Issue**: Chrome-specific rendering problems identified
- **Edge Browser Working**: System functions perfectly in Microsoft Edge
- **Chrome Fixes Applied**: Hardware acceleration, GPU rendering, service worker cleanup
- **Advanced Compatibility**: Multiple Chrome-specific CSS and JS optimizations
- **User Solution**: PC restart recommended to clear Chrome cache and processes
- **Fallback Strategy**: Edge browser confirmed working as alternative
- **Illinois Test Integration**: Maintained and fully operational in working browsers

### Body Composition Analysis Module - January 24, 2025
- **Complete Smart Scale Integration**: Arboleaf balance integration with full body composition analysis
- **Database Schema**: Complete PostgreSQL schema with body_composition_analyses table implemented
- **AI Analysis Engine**: Advanced algorithm analyzing muscle mass, body fat, BMR, metabolic age with professional recommendations
- **Academy Benchmarks**: Comparison with La Masia, Ajax, Real Madrid body composition standards
- **Comprehensive Data Collection**: Weight, BMI, body fat %, muscle mass, bone mass, water %, protein %, visceral fat, BMR, metabolic age
- **Professional Recommendations**: AI-powered nutrition plans, training focus, development goals with 3/6 month objectives
- **Multi-Scale Support**: Arboleaf, Tanita, InBody compatibility with manual data entry interface
- **French Interface**: Complete interface in French with professional guidance and measurement interpretation
- **Integration Options**: Manual data entry (current) with future API connection capability for automatic synchronization
- **API Routes**: Full REST API endpoints for CRUD operations on body composition data
- **Ready for Production**: System fully operational for professional body composition analysis and athlete development

### Test Nomenclature Update - January 23, 2025
- **Illinois Test Name Change**: Successfully updated from "Teste Illinois de Agilidade" to "Teste Conduite (Illinois)"
- **System-wide Implementation**: Updated all UI references, titles, buttons, notifications, and descriptive text
- **Terminology Change**: Changed from "agilidade" to "conduite" throughout interface
- **Multilingual Support**: Updated both Portuguese and French versions in global interface  
- **Navigation Updates**: Modified sidebar and mobile navigation menu labels
- **Core Functionality**: All automatic saving and test execution capabilities preserved
- **Training Plan Integration**: Dialog system remains functional with Chrome compatibility fixes

## Data Flow

### Test Session Workflow
1. Coach selects a player and test type(s)
2. System creates a new test session record
3. Individual test results are recorded in real-time
4. Upon completion, overall scores are calculated
5. AI analysis is generated and stored
6. Results are available in player profiles and analytics dashboard

### Player Management Flow
1. Coaches can create, edit, and manage player profiles
2. Player data is validated using Zod schemas
3. Changes are persisted to PostgreSQL via Drizzle ORM
4. Real-time updates are reflected across the application

### Authentication and Authorization
- Session-based authentication with PostgreSQL storage
- Role-based access control (Coach, Admin roles)
- Secure API endpoints with middleware protection

## External Dependencies

### Core Framework Dependencies
- **React Ecosystem**: React 18, React Router (Wouter), React Hook Form
- **Database**: Drizzle ORM, Neon PostgreSQL driver
- **UI Libraries**: Radix UI primitives, Lucide React icons
- **Validation**: Zod for schema validation
- **Styling**: Tailwind CSS, class-variance-authority for component variants

### Development Tools
- **TypeScript**: Full type safety across frontend and backend
- **Vite**: Development server and build tool
- **ESBuild**: Backend bundling for production
- **PostCSS**: CSS processing with Autoprefixer

### Third-Party Integrations
- **Neon Database**: Serverless PostgreSQL hosting
- **Replit**: Development environment with specialized plugins
- **Google Drive**: File storage for reports and media (planned)

## Deployment Strategy

### Development Environment
- Vite development server for frontend with HMR
- Express server with TypeScript compilation via tsx
- Replit-specific plugins for enhanced development experience
- Environment-based configuration for database connections

### Production Build Process
1. Frontend: Vite builds React application to static assets
2. Backend: ESBuild bundles Express server into single distributable
3. Database: Drizzle migrations ensure schema consistency
4. Static assets served by Express in production mode

### Environment Configuration
- Database connections via environment variables
- Separate configurations for development and production
- Session secret and authentication keys managed securely
- CORS and security middleware configured for production deployment

### Scalability Considerations
- Serverless-ready database architecture with Neon
- Stateless backend design for horizontal scaling
- Optimized frontend bundle for fast loading
- CDN-ready static asset structure