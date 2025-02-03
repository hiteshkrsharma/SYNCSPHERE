# Full-stack Jira 
An end-to-end full-stack Jira clone that features workspaces, projects, epics, tasks, kanban boards, calendars, role-based access control, and more. Built with Next.js, Appwrite SDK, Shadcn UI, TailwindCSS, 
and integrated with Hono.js for API endpoints.

## Key Features
   🏢 Workspaces: Multiple workspaces can be created and managed.
   
   📊 Projects / Epics: Organize your work into projects and break them down into epics.
   
   ✅ Tasks: Create, edit, delete, and track individual tasks.
   
   📋 Kanban Board View: Visualize and manage tasks in a drag-and-drop Kanban board view.
   
   🗃️ Data Table View: View and manage tasks in a sortable and filterable table.
   
   📅 Calendar View: Schedule and manage tasks with an integrated calendar view.
   
   ✉️ Invite System: Invite team members to workspaces and projects.
   
   ⚙️ Workspace and Project Settings: Configure workspace and project details, permissions, and preferences.
   
   🖼️ Image Uploads: Upload images for task attachments and user avatars.
   
   🔌 Appwrite SDK Integration: Utilizes Appwrite SDK for backend services, including authentication and file management.
   
   ⚛️ Next.js 14 Framework: Built with Next.js 14 for server-side rendering and fast performance.
   
   🎨 Shadcn UI & TailwindCSS Styling: A beautiful, consistent UI using Shadcn components and TailwindCSS.
   
   🔍 Advanced Search and Filtering: Quickly search tasks, projects, and epics with advanced filtering options.
   
   📈 Analytics Dashboard: A visual dashboard to track project and task progress.
   
   👥 User Roles and Permissions: Role-based access control for different levels of access.
   
   🔒 Authentication: OAuth and email-based authentication for secure user login.
   
   📱 Responsive Design: Fully mobile-responsive for efficient task management on-the-go.
   
   🚀 API with Hono.js: A fast API built with Hono.js to manage backend data.
## Tech Stack
  ### Frontend:
   
   Next.js 14
   
   TailwindCSS
   
   Shadcn UI
### Backend:
   Appwrite SDK (for authentication, databases, and file uploads)
   
   Hono.js (for API endpoints)
   
   Authentication: OAuth (Google, GitHub) & Email-based authentication
   
   Database: Appwrite Database (for storing tasks, projects, users, etc.)
   
   Styling: TailwindCSS, Shadcn UI
   
   Hosting: Vercel (Frontend), Appwrite (Backend)
### Installation:
   To get started with the project locally, follow these steps:

1. Clone the repository:
   
   bash
   
   Copy
   
   [git clone https://github.com/your-username/jira-clone.git]
   
   cd jira-clone
3. Install dependencies:
   bash
   Copy
   npm install
4. Set up environment variables:
   
   Create a .env.local file in the root of the project and add the following environment variables:

   bash
   
   Copy
   
   NEXT_PUBLIC_APPWRITE_URL=your-appwrite-url
   
   NEXT_PUBLIC_APPWRITE_PROJECT_ID=your-appwrite-project-id
   
   NEXT_PUBLIC_APPWRITE_DATABASE_ID=your-appwrite-database-id
   
   NEXT_PUBLIC_APPWRITE_STORAGE_BUCKET_ID=your-appwrite-storage-bucket-id
   
   NEXT_PUBLIC_OAUTH_GOOGLE_CLIENT_ID=your-oauth-google-client-id
   
   NEXT_PUBLIC_OAUTH_GOOGLE_SECRET=your-oauth-google-secret
   
   NEXT_PUBLIC_OAUTH_GITHUB_CLIENT_ID=your-oauth-github-client-id
   
   NEXT_PUBLIC_OAUTH_GITHUB_SECRET=your-oauth-github-secret
6. Run the development server:
   
   bash
   
   Copy
   
   npm run dev
   
   Visit http://localhost:3000 to see the app in action.

## Usage:

#### Workspaces:
Create and manage different workspaces to segregate projects and tasks. Each workspace can have its own set of projects and members.
     

#### Projects / Epics:
Organize your tasks into projects, and group them into larger epics. You can track progress and manage resources at both the project and epic levels.
     

#### Tasks:
Create, assign, update, and delete tasks. Track their status (To Do, In Progress, Done) across different views (Kanban, Data Table, Calendar).

#### Kanban Board:
Drag-and-drop tasks between different columns (To Do, In Progress, Done) for easy task management and progress tracking.

#### Calendar View:
View and schedule tasks on a calendar for a time-based overview of your workload.

#### Invite System:
Invite team members to join specific workspaces and projects. Control user roles and permissions.

#### User Roles & Permissions:
Define different user roles (Admin, Member) with different levels of access to workspaces, projects, and tasks.

#### Analytics Dashboard:
Access real-time analytics for tasks, projects, and overall workspace progress.

#### API
The backend is powered by Hono.js, offering a set of RESTful API endpoints to manage tasks, projects, users, and workspaces. The API allows for:

Creating, updating, and deleting tasks and projects.

Managing users and roles.

Handling authentication (OAuth and email).

Uploading and downloading files (avatars, attachments).

## Contributing
We welcome contributions! To contribute to this project:

### Fork the repository:
Clone your fork to your local machine

Create a new branch for your feature or bugfix

Make your changes and commit them

Push to your fork and create a pull request
## License
This project is licensed under the MIT License - see the LICENSE file for details.






