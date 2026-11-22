"""All text on the site. Edit here, then run: python3 build/build.py

Body blocks for a project page:
  ("h", "Heading")
  ("p", "Paragraph; inline HTML like <b> and <code> is allowed")
  ("ul", ["item", "item"])
  ("img", "path/under/Portfolio/projects.png", "caption")
  ("note", "small grey note")
"""

SITE = {
    "name": "Sathish Kumar",
    "role": "Full Stack Software Engineer",
    "location": "Chennai, India",
    # Change this to your custom domain once you have one (used for share previews).
    "url": "https://sathishr424.github.io/",
    "year": "2026",
    "email": "rsathishikumar3@gmail.com",
    "github": "https://github.com/Sathishr424",
    "linkedin": "https://linkedin.com/in/sat-this-h",
    "leetcode": "https://leetcode.com/u/sat_this_h/",
    "upwork": "https://www.upwork.com/freelancers/~01b87d2baf21208fc5",
    "resume_pdf": "Sathish-Kumar-Resume.pdf",
    "resume_source": "/home/sathish/Documents/Sathish Resume 22th Nov 2026.pdf",
    "headline": "I build web apps, real‑time systems and the data pipelines behind them.",
    # Same as the resume summary.
    "intro": (
        "Full Stack Software Engineer with 5 years of experience designing, building and shipping production web "
        "applications, backend services, data pipelines and real-time systems end to end. Delivered 90+ client projects "
        "as a Top Rated Upwork engineer, owning requirements, architecture, implementation and deployment. Comfortable "
        "extending large legacy codebases (Java optimization engine, Vue.js/Node.js platform at Pando) as well as building "
        "systems from scratch, including a real-time voice AI pipeline backed by 800+ automated tests. Hands-on with "
        "Docker, Kubernetes, Terraform and CI/CD, and strong in algorithms (LeetCode Guardian, max rating 2144)."
    ),
    "meta_description": (
        "Sathish Kumar, full stack software engineer in Chennai. Case studies: a real-time voice "
        "AI interviewer, a scalable chat platform, a canvas text editor engine, and client work "
        "in scraping and e-commerce. LeetCode Guardian, max rating 2144 (top 1%)."
    ),
    "looking_for": (
        "I'm looking for a full-stack or backend role on a product team, working on real-time "
        "systems, data pipelines or AI-powered features. I also take freelance projects."
    ),
    # Skill chips above the projects; each project's "skills" list decides which chips light it up.
    "filters": ["Python", "TypeScript", "React", "Vue.js", "Node.js", "WebSockets", "Redis", "Docker", "Kubernetes", "Laravel", "MySQL", "Scraping", "Canvas", "AI"],
    "stats": [
        ("5 yrs", "building and shipping software"),
        ("90+", "client projects delivered"),
        ("Top Rated", "on Upwork"),
        ("2144", "LeetCode Guardian, top 1%"),
    ],
}

EXPERIENCE = [
    {
        "when": "Jan 2022 – Present",
        "role": "Full Stack Software Engineer, Independent Contractor",
        "where": "Upwork (Top Rated) & Fiverr · India",
        "points": [
            "Delivered 90+ client projects across e-commerce, legal, media and healthcare, owning the full lifecycle from requirements and architecture to implementation, deployment and client handover.",
            "Designed and built 50+ product-data extraction pipelines in Python (Requests, BeautifulSoup, Selenium) and Node.js (Puppeteer) with proxy management, delivering structured CSV/JSON for price comparison and catalog systems.",
            "Automated bulk court-filing retrieval and built PDF extraction tooling that converts documents into structured JSON and Excel datasets, replacing manual data entry for legal clients.",
            "Shipped end-to-end web applications, Chrome extensions and browser-based audio recording solutions, translating loosely defined client needs into maintainable, production-ready systems.",
        ],
    },
    {
        "when": "Jan 2026 – Jun 2026",
        "role": "Full Stack Developer Intern",
        "where": "Pando · Chennai",
        "points": [
            "Implemented a \"stacking norms\" constraint in a Java truck-loading optimization engine so generated load plans never place items on top of designated non-stackable items.",
            "Refactored legacy code across the Java codebase to support the new constraint while preserving the existing structure, backward compatibility and optimization behavior.",
            "Shipped full-stack features on a production legacy platform spanning the Vue.js UI, Node.js backend logic and MongoDB data model changes.",
        ],
    },
    {
        "when": "Aug 2017 – Nov 2021",
        "role": "Structural Steel Detailer",
        "where": "Cistron Infotek & Moldtek Technologies Pvt. Ltd · Chennai",
        "points": [
            "Produced structural steel erection and shop drawings in Tekla Structures, following project specifications and applicable engineering standards.",
        ],
    },
]

SKILLS = [
    # Copied from "Sathish Resume 22th Nov 2026.pdf". Keep these in sync with the resume.
    ("Languages", ["JavaScript", "TypeScript", "Python", "Java", "C/C++", "PHP", "SQL", "Bash"]),
    ("AI & LLM Engineering", ["LLM API Integration", "Tool/Function Calling", "Model Context Protocol (MCP)",
        "Agent-to-Tool Integration", "Agentic AI Workflows", "Multi-Step Agent Workflows", "Prompt & Context Engineering",
        "AI Coding Agents", "Claude Code", "AI-Assisted Development", "Retrieval-Augmented Generation (RAG)",
        "Advanced RAG Techniques", "Embeddings", "Vector Databases", "Similarity Search", "LangChain",
        "Hugging Face Transformers", "Gradio", "LLM Evaluation"]),
    ("Frontend", ["React", "Next.js", "Vue", "HTML", "CSS", "Tailwind CSS"]),
    ("Backend", ["Node.js", "Express.js", "Laravel", "REST APIs", "Socket.IO"]),
    ("Databases & Caching", ["PostgreSQL", "MySQL", "MongoDB", "Redis", "Prisma ORM"]),
    ("DevOps & Cloud", ["Linux", "Docker", "Docker Compose", "Kubernetes", "Helm", "Jenkins", "GitHub Actions", "Terraform",
        "Nginx", "AWS", "Oracle Cloud"]),
    ("System Design & Algorithms", ["System Design (HLD, LLD)", "Distributed Systems", "Database Design",
        "Data Structures & Algorithms", "LeetCode Guardian (Max Rating 2144)"]),
    ("Web Scraping & Automation", ["Selenium", "Puppeteer", "BeautifulSoup", "Browser Automation", "Proxy Management",
        "Structured Data Extraction"]),
]

PROJECTS = [
    # ------------------------------------------------------------------ Mock AI
    {
        "slug": "mock-ai",
        "title": "Mock AI",
        "tagline": "A voice interviewer that talks back: practice interviews out loud and get a scored report with a stronger answer.",
        "kind": "Personal project", "kind_key": "personal", "year": "2026", "featured": True,
        "cover": "mockai/cover-upwork.png",
        "tags": ["Python", "FastAPI", "WebSockets", "TypeScript", "Whisper", "Ollama", "Docker", "Playwright"],
        "skills": ["Python", "TypeScript", "React", "WebSockets", "Docker", "AI"],
        "facts": [("Role", "Sole developer"), ("Built", "Nov 2026"), ("Time to first audio", "3–5 seconds"),
                  ("Tests", "800+ automated"), ("Runs on", "A 6 GB GPU or cloud APIs")],
        "links": [],
        "link_note": "Code walkthrough and demo available on request.",
        "body": [
            ("h", "The problem"),
            ("p", "Reading interview questions is easy. Answering them out loud, under a little pressure, is not. Most practice "
                  "tools are text chat, and they never show you <i>how</i> your answer could have been better."),
            ("h", "What it does"),
            ("p", "Four modes from the home page: a recruiter call, a technical round, a behavioural round, and a sales call where "
                  "the roles flip and the AI plays a prospect while you pitch your own offer. For a technical round you pick the "
                  "role, level, difficulty and skills, from 39 skills in 7 groups."),
            ("gallery", [("mockai/01-setup-technical-interview.png", "Set up a technical round."),
                         ("mockai/02-equipment-check.png", "A microphone and speaker check before it starts.")]),
            ("p", "The interviewer asks one question at a time, follows up when an answer is vague and stops talking the moment you "
                  "talk over it. Asking it to explain a question doesn't use the question up, and, if that option is on, it can "
                  "close the interview itself when you ask to stop or run out of time."),
            ("gallery", [("mockai/04-live-question-and-answer.png", "The current question, live."),
                         ("mockai/05-live-interview-transcript.png", "The transcript builds as you talk.")]),
            ("h", "The report"),
            ("ul", ["a score out of 100 and a mark out of 10 for each of the round's own criteria",
                    "strengths, what to work on, and a note of two or three sentences under every answer",
                    "a stronger rewrite of one of your answers",
                    "a recording of both voices with the thinking gaps trimmed, playable from any line or downloadable as a <code>.wav</code>",
                    "buttons to rewrite the whole report or only the notes, keeping the old version if the model fails"]),
            ("gallery", [("mockai/06-report-score-and-criteria.png", "Score, summary and per-criterion marks."),
                         ("mockai/07-report-strengths-and-stronger-answer.png", "Strengths and a stronger answer."),
                         ("mockai/09-transcript-with-recording.png", "The recording, linked to each transcript line."),
                         ("mockai/11-transcript-per-answer-feedback.png", "Feedback under every answer.")]),
            ("h", "How it works"),
            ("p", "The browser streams the microphone to a FastAPI backend over one WebSocket. The backend decides when you've "
                  "finished speaking, turns speech into text, has the language model write the reply and speaks it back sentence "
                  "by sentence as it's generated. Every stage sits behind an interface, so each one runs locally or in the cloud "
                  "by changing a setting:"),
            ("ul", ["<b>Voice detection:</b> Silero, always on your machine",
                    "<b>Speech to text:</b> Whisper through Hugging Face Transformers on the GPU, or Cartesia or ElevenLabs",
                    "<b>The interviewer:</b> any model served by Ollama, locally or on Ollama Cloud",
                    "<b>Text to speech:</b> Chatterbox on the GPU with its own voice for each round, or Cartesia, ElevenLabs, or Underdog Woof on the CPU"]),
            ("p", "In the default local setup nothing is sent anywhere, and the recording never leaves the browser."),
            ("h", "The hard parts"),
            ("ul", ["<b>Turn-taking.</b> Telling when someone has finished speaking, not just paused to think, without cutting them off.",
                    "<b>Interruptions.</b> When you talk over the interviewer, the screen and the model's memory keep only the words it actually said before you cut in.",
                    "<b>The recording.</b> Merging both voices into one timeline, trimming the gaps, and linking each transcript line to its point in the audio, all in the browser.",
                    "<b>Useful scores from a small model.</b> Schema-validated JSON with one retry and per-round criteria checked on the server. It returned a valid report in every test run, and strong interviews scored 75–88 while weak ones scored 13–20.",
                    "<b>Prompts per round.</b> Each round has its own prompt and closing prompt on top of shared rules, so the model writes fresh questions from topics instead of reading a fixed list."]),
            ("h", "How I built it"),
            ("ul", ["Every feature started as a written plan and ended with a test log of what was checked and measured.",
                    "Test-first with Claude Code: each test was seen failing before the code was written. About 560 backend tests, 187 client unit tests and 92 Playwright end-to-end tests, including accessibility checks in light and dark mode.",
                    "A stub mode runs the whole suite without any models; smoke tests run against the real ones. With Cartesia on both ends, the first audio came 3.9 seconds after the last word.",
                    "Multi-stage Docker builds and Compose profiles for the local-GPU and cloud setups."]),
        ],
    },
    # ------------------------------------------------------------------ SatChat
    {
        "slug": "satchat",
        "title": "SatChat",
        "tagline": "A real-time chat platform built to scale out, with presence, read receipts, files and GIFs, deployed on Kubernetes.",
        "kind": "Personal project", "kind_key": "personal", "year": "2026", "featured": True,
        "cover": "satchat/cover-upwork.png",
        "tags": ["React", "TypeScript", "Node.js", "Express", "Socket.IO", "Redis", "PostgreSQL", "Prisma", "Kubernetes", "Jenkins"],
        "skills": ["React", "TypeScript", "Node.js", "WebSockets", "Redis", "Docker", "Kubernetes"],
        "facts": [("Role", "Sole developer"), ("Built", "Sep–Oct 2026"), ("Services", "7 containers behind Nginx"),
                  ("Deploy", "Docker Compose or Kubernetes"), ("Cloud", "AWS, provisioned with Terraform")],
        "links": [("Live demo", "https://satdevopsdummies.xyz/"), ("Source on GitHub", "https://github.com/Sathishr424/ChatApp_plus_devops")],
        "body": [
            ("h", "What it is"),
            ("p", "A simplified Slack or Discord: one-to-one chats and group channels with live delivery, presence, typing "
                  "indicators, read receipts, file sharing, GIFs, message search and email alerts. It works on desktop and mobile, "
                  "and a live demo is running."),
            ("gallery", [("satchat/screenshots/d02-group-chat-file-sharing.png", "A group chat with shared files."),
                         ("satchat/screenshots/d05-direct-message-presence-typing.png", "Presence and typing in a direct message."),
                         ("satchat/screenshots/d06-unread-badges-and-read-receipts.png", "Unread badges and read receipts."),
                         ("satchat/screenshots/d08-message-search.png", "Search across messages.")]),
            ("ul", ["<b>Accounts</b> with JWT sign-in and profiles",
                    "<b>Groups</b> you create and name, plus one-to-one chats",
                    "<b>Files and images</b> through their own storage service, and a GIF picker",
                    "<b>Email alerts</b> sent by the backend's mail service"]),
            ("h", "Jump to any search result in O(log n)"),
            ("p", "This is the strongest piece of algorithm work in the project. Message search returns only the IDs of matching "
                  "messages, newest first, a page at a time. When you step to a result that isn't loaded yet, the app has to "
                  "bring in everything between what's on screen and that message. Loading page after page until it appears "
                  "would take hundreds of requests in a long chat. Instead, the backend finds the message's exact position first:"),
            ("ul", ["<b>Exponential (galloping) search.</b> From the edge of what's already loaded, it probes offsets 1, 2, 4, 8 and onwards, each probe a one-row query, until it passes the target message.",
                    "<b>Binary search</b> inside that last range then finds the exact offset of the message.",
                    "<b>One request</b> loads exactly the messages up to it, and the pagination state carries on from there, so scrolling back through older messages keeps working."]),
            ("p", "For a message 10,000 messages back, that's about 28 one-row queries instead of 500 page loads. The same "
                  "search works for direct chats and groups."),
            ("h", "Everything loads lazily, through one hook"),
            ("p", "Nothing in SatChat loads in full: the messages, the search results, the Recent, Unread and Groups lists, the "
                  "people picker when you create a group, and GIF search all load a page at a time as you scroll. All of them use "
                  "one generic React hook, <code>usePagination&lt;T&gt;</code>. Each list only supplies the function that fetches "
                  "a page; the hook owns the cursor, \"has more\", the loading state, a guard against duplicate requests, and a "
                  "400 ms debounced search that resets the list. Adding a new lazy list is a few lines."),
            ("h", "Recent, Unread and Groups on the backend"),
            ("ul", ["<b>One row does three jobs.</b> The unread table keeps, per conversation, the unread count, the latest message and the time of last activity. So the whole sidebar preview (last message, edited or deleted, GIF, attachment count, unread badge) comes from one query with joins, and unread counts are never counted from the messages.",
                    "<b>Keyset pagination, not OFFSET.</b> The cursor is the pair (last activity, id), so pages stay stable while new messages arrive and a chat is never repeated or skipped. Contacts you've never messaged sort last and still page correctly.",
                    "<b>People and groups in one list.</b> Recent and Unread run the people query and the groups query with the same cursor, merge the two sorted results by last activity and trim to the page size.",
                    "<b>No total counts for paging.</b> Every query asks for one extra row; if it comes back, there's another page.",
                    "<b>One query builder per kind.</b> People and groups each have a single SQL builder with composable WHERE parts for the cursor, unread-only and search, so Recent, Unread, Groups and all their searches are the same query with different filters."]),
            ("h", "Code structure"),
            ("ul", ["<b>Layered backend:</b> controllers, services and repositories, with request DTOs validated by middleware before a handler runs, response DTOs shaping what goes out, and typed exceptions turned into HTTP errors in one place.",
                    "<b>Shared domain code:</b> the REST API and the socket server import the same models, DTOs and Redis connection from one shared package.",
                    "<b>Typed pub/sub on the client:</b> one message system fans socket events (new, edited, deleted and seen messages, typing, presence) out to subscribers, so components react to events without touching the socket."]),
            ("img", "satchat/realtime-details.png", "The details that make chat feel live."),
            ("h", "How it's built"),
            ("img", "satchat/architecture.png", "Seven containers, four written for this project, behind Nginx."),
            ("ul", ["<b>Separate REST and WebSocket tiers.</b> REST is stateless and easy to scale; socket connections are long-lived and scale differently. Both share one domain codebase.",
                    "<b>Redis to scale sockets horizontally.</b> Any socket server can emit to a room, and Redis pub/sub relays it to whichever server holds the recipient's connection.",
                    "<b>Presence that survives many tabs.</b> Each user has a set of live socket IDs in Redis; they go offline only when the last one disconnects, and only that final disconnect writes \"last seen\" to Postgres.",
                    "<b>Persist, then broadcast.</b> A message is saved before anyone hears about it, so the database defines the order.",
                    "<b>Unread counts stored, not counted.</b> Sending increments a counter and opening the chat resets it, so the sidebar never counts rows.",
                    "<b>A schema that evolved safely.</b> PostgreSQL through Prisma, changed over 28 migrations.",
                    "<b>Build once, deploy anywhere.</b> The client reads its URLs at container start, so one image runs in every environment."]),
            ("img", "satchat/presence-across-devices.png", "Presence stays correct across tabs and devices."),
            ("h", "Shipping it"),
            ("p", "There are two ways to deploy it, each with its own Jenkins pipeline that builds and pushes the images first:"),
            ("ul", ["<b>One VM:</b> Terraform creates an AWS EC2 instance and Docker Compose runs the whole stack on it.",
                    "<b>A Kubernetes cluster:</b> Terraform creates a control-plane node and two workers on EC2, and scripts set them up with kubeadm and Calico and join the workers.",
                    "<b>Helm:</b> seven charts, one per component. The API, socket, storage and client tiers autoscale with Horizontal Pod Autoscalers.",
                    "<code>/health</code> and <code>/ready</code> checks on every service, and Nginx with SSL in front."]),
            ("img", "satchat/features-mobile.png", "On mobile."),
        ],
    },
    # ------------------------------------------------------------------ Text editor
    {
        "slug": "text-editor-engine",
        "title": "Text Editor Engine",
        "tagline": "A multi-page document editor built from scratch on HTML Canvas, with its own text model, layout, rendering, undo and live collaboration.",
        "kind": "Personal project", "kind_key": "personal", "year": "2025",
        "cover": "text-editor-engine/01-cover.png",
        "tags": ["TypeScript", "HTML Canvas", "Data structures", "Socket.IO", "Node.js", "Command pattern", "Pub/sub"],
        "skills": ["TypeScript", "Canvas", "WebSockets", "Node.js"],
        "facts": [("Role", "Sole developer"), ("Built", "Oct–Nov 2025"), ("Core libraries", "None"),
                  ("Edits at the cursor", "O(1)"), ("Collaboration", "Live, ordered by the server")],
        "links": [("Source on GitHub", "https://github.com/Sathishr424/DistributedRealTimeCollaborativeDocumentEditor")],
        "body": [
            ("h", "Why build it"),
            ("p", "Most web editors sit on <code>contenteditable</code> or a library like ProseMirror. I wanted to understand what "
                  "those hide, so I wrote every layer myself: how text is stored, how it becomes lines and pages, how it's painted, "
                  "and how the cursor, selection, undo and other people's edits stay consistent through all of it."),
            ("h", "What it does"),
            ("ul", ["<b>Multi-page documents.</b> Text flows onto a new page as you type and empty pages disappear. Each page is its own canvas, and clicks map back to the right page, row and column.",
                    "<b>Cursor and selection.</b> Arrow keys, Shift and Ctrl combinations, word jumps and deletes, select all and drag selection, across wrapped lines and page breaks.",
                    "<b>Undo and redo</b> built on operations that each have an exact inverse.",
                    "<b>Real-time collaboration.</b> Several people edit the same document live, shared by link with read or write access."]),
            ("h", "The text model: two stacks that meet at the cursor"),
            ("p", "The document is stored as two character stacks: everything before the cursor on one, everything after it on the "
                  "other in reverse. It's the idea behind a gap buffer. Typing is a push and Backspace or Delete is a pop, so an edit "
                  "at the cursor is O(1) however long the document is. Moving the cursor k characters moves k characters from one "
                  "stack to the other."),
            ("ul", ["<b>Line data split the same way.</b> For every line the model keeps its length and how many screen rows it wraps to, in two more stacks on either side of the cursor's line. Crossing a newline moves one record from one side to the other.",
                    "<b>Running totals, never recounted.</b> It keeps the number of wrapped rows above and below the cursor and adjusts them on every insert, delete and newline. So the cursor's on-screen row and column come from arithmetic in O(1), not from scanning the document.",
                    "<b>A hand-written deque</b> on a doubly linked list holds the line lengths, with O(1) push and pop at both ends. Lines cross over at the back of one side and the front of the other, so both ends are needed.",
                    "<b>One model, two places.</b> The collaboration server keeps its copy of each document in the same text model, so the client and server apply edits the same way."]),
            ("img", "text-editor-engine/03-text-model-and-undo.png", "Two stacks at the cursor, and undo built from invertible operations."),
            ("h", "Undo and redo as invertible operations"),
            ("ul", ["Every edit is recorded as one of four operations: an insert or a delete, to the left or the right of the cursor. Each one knows how to apply itself and has an exact inverse.",
                    "Undo pops the history stack, applies the operation and pushes its inverse onto the redo stack. Redo does the same in the other direction, and a new edit clears the redo stack.",
                    "Operations can be chained, so a group of edits undoes as one step. Each one also stores where the cursor was, so undo puts the cursor back too."]),
            ("h", "Painting only what's on screen"),
            ("p", "The renderer never draws the whole document. From the scroll position it works out, with arithmetic alone, which "
                  "page and rows are in view, adds a buffer of 100 rows above and below, and paints only that window: clearing those "
                  "rows, drawing their characters, then drawing the selection over them. Pages are separate canvases created when text "
                  "overflows and removed when one empties, so the drawing work depends on the window, not on the document's length."),
            ("img", "text-editor-engine/04-lazy-rendering.png", "Only the rows in view, plus a 100-row buffer, are painted."),
            ("h", "Architecture"),
            ("img", "text-editor-engine/02-architecture.png", "Input flows one way; the renderer only listens for events."),
            ("ul", ["<b>One orchestrator, injected parts.</b> A document service builds the layout engine, page controller, cursor, text controller, input controller and renderer, and hands each one the parts it needs through its constructor. Nothing reaches for a global, so each part can be replaced or tested on its own.",
                    "<b>Command pattern for every shortcut.</b> A registry maps 20 key combinations (arrows, their Shift and Ctrl versions, Backspace, Delete, Enter, Tab, undo, redo and select all) to command classes that share one constructor. A new shortcut is one class and one line in the registry.",
                    "<b>Two event buses.</b> Text and cursor changes go out on one bus and render requests on another. The renderer only subscribes, so nothing calls it directly.",
                    "<b>Key and clipboard handling kept apart.</b> Key combinations are tracked in their own state object, and copy, cut and paste have their own handlers, so the commands never deal with raw browser events."]),
            ("h", "Real-time collaboration"),
            ("ul", ["An edit doesn't change the local text straight away. It goes to the server with the document version it was made against.",
                    "The server keeps a log of operations by version. If other people edited since that version, it shifts the incoming edit's position past every newer insert and delete (operational transformation by index), applies it, bumps the version and broadcasts it.",
                    "Every client, the sender included, applies the server's ordered version, so everyone ends up with the same text. If someone else inserts above your cursor, your cursor moves with your text.",
                    "The server saves each document to disk at most once a second and caps how many people can join one document."]),
        ],
    },
    # ------------------------------------------------------------------ Resume builder
    {
        "slug": "resume-builder",
        "title": "Resume Builder",
        "tagline": "A resume builder with a live A4 preview, four templates, drag-to-reorder sections and PDF export, in plain TypeScript.",
        "kind": "Personal project", "kind_key": "personal", "year": "2026",
        "cover": "resume-builder/light/cover-upwork.png",
        "tags": ["TypeScript", "No UI framework", "Vite", "Tailwind CSS", "React (templates)"],
        "skills": ["TypeScript", "React"],
        "facts": [("Role", "Sole developer"), ("Built", "Nov 2026"), ("Templates", "4, more on the way"),
                  ("Section types", "15")],
        "links": [],
        "link_note": "Code walkthrough available on request.",
        "body": [
            ("h", "The problem"),
            ("p", "Most resume builders hide the PDF behind a sign-up, or show the result only after you finish the form. I wanted one "
                  "where you see the real page while you type and can download it straight away, with no account."),
            ("h", "What it does"),
            ("ul", ["<b>Editor</b> for 15 section types: employment, education, projects, skills with a level slider, languages, links, certificates, custom sections and more. Sections and the entries inside them can be dragged into order, renamed and deleted.",
                    "<b>Live preview</b> of an A4 page beside the form, scaled to fit, in one of four templates.",
                    "<b>PDF export</b> through an A4 print window with margins repeated on every page, so long resumes break cleanly.",
                    "<b>Autosave</b> to local storage a second after you stop typing, plus JSON export and import, so nothing needs a server or an account.",
                    "<b>Phones</b> get Edit and Preview tabs, and there's a light and dark theme."]),
            ("img", "resume-builder/light/editing.png", "The form and the A4 page stay in sync."),
            ("img", "resume-builder/light/screenshots/builder-add-section.png", "Add any of the 15 section types, then drag it into place."),
            ("h", "Four templates, one resume"),
            ("p", "Switching templates never touches your data: the same resume renders in each one, and the preview updates at once."),
            ("img", "resume-builder/light/templates.png", "Four templates, one set of data, and the 15 section types every template supports."),
            ("p", "Each template is a single React component file. Adding one means creating the file and registering it in the "
                  "template list; it then appears in the gallery and renders the same resume data. More templates are on the way."),
            ("h", "How it's built"),
            ("img", "resume-builder/light/how-it-works.png", "Plain TypeScript classes; React only renders templates to static HTML."),
            ("p", "There's no UI framework. Each section is a TypeScript class on a shared <code>Draggable</code> base that handles "
                  "the drag handle, drop placeholder, reordering and delete. Every edit notifies a pub/sub manager that debounces to "
                  "one refresh a second after typing stops; the store saves the resume as JSON and the preview re-renders the "
                  "chosen template with React's <code>renderToStaticMarkup</code>. The print window gets that same HTML, so the PDF "
                  "matches the preview. A small router serves the gallery, the builder and a 404 page."),
        ],
    },
    # ------------------------------------------------------------------ Scraping
    {
        "slug": "ecommerce-scraping",
        "title": "E-commerce Scraping",
        "tagline": "Product catalogs from 51 online stores, 300k+ products in total, delivered as import-ready CSV and Excel files.",
        "kind": "Client work", "kind_key": "client", "year": "2022 – now",
        "cover": "scraping/cover-upwork.png",
        "tags": ["Python", "Selenium", "undetected-chromedriver", "BeautifulSoup", "Proxies", "pandas"],
        "skills": ["Python", "Scraping"],
        "facts": [("Stores", "51"), ("Products", "300k+"), ("Largest store", "77k+ products"),
                  ("Delivered as", "CSV and Excel"), ("Since", "2022")],
        "links": [],
        "body": [
            ("h", "The problem"),
            ("p", "Retailers, resellers and catalog teams needed product data from other stores: whole catalogs with prices, specs and "
                  "images, in a format they could import. Copying it by hand would take months, and every site is built differently."),
            ("h", "What I built"),
            ("p", "A custom scraper for each store, from big retailers like Lowe's, Menards, Northern Tool and Acme Tools down to small brand sites:"),
            ("ul", ["<b>Finding products</b> by walking category pages or sitemaps, or from the client's own URL or SKU list.",
                    "<b>Fetching pages</b> with Requests and BeautifulSoup for static sites, and a real browser for dynamic sites, infinite scroll, reCAPTCHA and heavily protected stores. Threads, proxies and rotating user agents kept big runs fast, and failed URLs were logged and retried.",
                    "<b>Extracting fields:</b> titles, SKUs, brands, categories, prices, sale prices and rebates, options, stock, shipping, specs as clean HTML, manuals, videos and images.",
                    "<b>Delivering</b> CSV or Excel files in the client's column format, with images downloaded and named to match."]),
            ("img", "scraping/stores-scraped.png", "51 stores, up to 77k+ products from one."),
            ("h", "The toolkit"),
            ("ul", ["<b>Static pages:</b> Python with Requests, cloudscraper and BeautifulSoup",
                    "<b>Dynamic and protected pages:</b> Selenium, SeleniumBase, undetected-chromedriver, selenium-wire and Playwright, plus Puppeteer in Node.js for some stores",
                    "<b>Speed and reliability:</b> concurrent.futures threads, rotating proxies, fake-useragent, logged and retried failures",
                    "<b>Output:</b> pandas and openpyxl, shaped to each client's import format"]),
            ("img", "scraping/how-it-works.png", "The pipeline, the fields delivered and the toolkit."),
            ("h", "Hard cases"),
            ("ul", ["<b>Rebates.</b> Menards shows an everyday price, a rebate and a price after rebate, and some prices only appear in the cart. Each became its own column, kept exactly as the store shows it.",
                    "<b>Huge crawls.</b> Northern Tool took 140k+ product URLs to crawl, which came down to 14k+ unique products once duplicates were removed.",
                    "<b>Bot protection.</b> Undetected Chrome, CAPTCHA handling, proxies and rotating user agents for the stores that block ordinary scrapers."]),
            ("h", "Scale"),
            ("p", "The largest jobs were 77k+ products from one tools retailer, 56k+ and 38k+ from others, and 140k+ product URLs crawled "
                  "on a single site. The smallest were brand sites with under 100 products."),
            ("img", "scraping/sample-outputs.png", "Real output files, first rows only."),
        ],
    },
    # ------------------------------------------------------------------ Price tracker
    {
        "slug": "price-tracker",
        "title": "E-commerce Price Tracker",
        "tagline": "A price-tracking site following thousands of products across 6 major US retailers, with live deals and price history.",
        "kind": "Client work · NDA", "kind_key": "client", "year": "2023 – 2024",
        "cover": "ecommerce-price-tracker/cover-upwork.png",
        "tags": ["Vue.js", "Laravel", "MySQL", "Bootstrap", "Scraping", "Cron"],
        "skills": ["Vue.js", "Laravel", "MySQL", "Scraping"],
        "facts": [("Role", "Most of the UI and backend, ~90% of scrapers"), ("Retailers", "6 major US stores"), ("Status", "Still live")],
        "links": [],
        "body": [
            ("h", "What it is"),
            ("p", "A price-tracking website that answers one question for shoppers: is this a good price? It shows a live deals feed "
                  "ranked by discount, filters by category, store, discount and price, and a product page with every store's current "
                  "price, the all-time low, a price history chart and past sales."),
            ("h", "My part"),
            ("p", "I built most of the Vue.js UI and the Laravel backend, including the full product page, and about 90% of the scrapers. "
                  "The site is still live and runs largely on my implementation."),
            ("h", "Keeping prices live"),
            ("img", "ecommerce-price-tracker/scraper-pipeline.png", "How the prices stay fresh."),
            ("ul", ["One scraper per retailer, run on cron schedules that store every price check",
                    "Rotating proxies so no single IP gets rate-limited or blocked",
                    "Live CAPTCHA solving when a site challenges a request",
                    "Headless browsers for retailers that render prices with JavaScript"]),
            ("h", "From prices to deals"),
            ("img", "ecommerce-price-tracker/price-signals.png", "From raw snapshots to deal signals."),
            ("p", "Every check is stored as a snapshot. From those, the backend works out each product's daily low across stores, "
                  "its all-time and 30-day lows, each store's sale runs, and the deals feed."),
            ("note", "The client and site are under NDA. Images are illustrations, not screenshots."),
        ],
    },
    # ------------------------------------------------------------------ Order builder
    {
        "slug": "custom-order-builder",
        "title": "Custom Order Builder",
        "tagline": "A 2-step product builder for a custom-apparel business that prices bulk orders live, so customers skip the quote.",
        "kind": "Client work · NDA", "kind_key": "client", "year": "Freelance",
        "cover": "custom-order-builder/cover-upwork.png",
        "tags": ["Laravel", "PHP", "MySQL", "JavaScript", "Shopify checkout"],
        "skills": ["Laravel", "MySQL"],
        "facts": [("Role", "Builder, pricing engine, backend and admin"), ("Pricing", "10 quantity tiers"), ("Checkout", "Shopify")],
        "links": [],
        "body": [
            ("h", "The problem"),
            ("p", "Custom apparel is usually sold by quote: the customer sends a logo, waits for a price and goes back and forth. "
                  "The client wanted customers to configure their order and see the exact price themselves, from one item to hundreds."),
            ("h", "What I built"),
            ("ul", ["<b>Step 1:</b> choose colors and enter quantities per size. Sold-out sizes are locked and a running total updates as you type.",
                    "<b>Step 2:</b> choose the decoration type and placement, upload a logo or enter text, and add extras.",
                    "<b>A pricing engine</b> with 10 quantity tiers, a price table per decoration type, tiered add-ons, a small-order fee and the savings shown against the single-item price.",
                    "<b>A Laravel and MySQL backend</b> for pricing, artwork uploads and orders, and an admin panel where the owners review every order."]),
            ("img", "custom-order-builder/pricing-engine.png", "The pricing engine. Numbers are illustrative."),
            ("h", "How it fits together"),
            ("img", "custom-order-builder/architecture.png", "The builder hands configured orders to the Shopify cart."),
            ("p", "The storefront and checkout run on Shopify. The builder hands the configured order to the Shopify cart, while the "
                  "Laravel backend keeps the pricing rules, artwork and order details behind it."),
            ("note", "Client under NDA. Images are illustrations, and prices shown are not the client's."),
        ],
    },
]


# Where each skill is shown on the site. Keys must match SKILLS exactly.
# Values are project slugs, or "pando" (Experience) / "leetcode" (LeetCode section).
# Skills not listed here show as plain chips with no link.
SKILL_PROOF = {
    "JavaScript": ["price-tracker", "custom-order-builder"],
    "TypeScript": ["mock-ai", "satchat", "text-editor-engine", "resume-builder"],
    "Python": ["mock-ai", "ecommerce-scraping"],
    "Java": ["pando"],
    "PHP": ["price-tracker", "custom-order-builder"],
    "SQL": ["satchat", "price-tracker", "custom-order-builder"],
    "LLM API Integration": ["mock-ai"],
    "Prompt & Context Engineering": ["mock-ai"],
    "Claude Code": ["mock-ai"],
    "AI-Assisted Development": ["mock-ai"],
    "Hugging Face Transformers": ["mock-ai"],
    "LLM Evaluation": ["mock-ai"],
    "React": ["mock-ai", "satchat", "resume-builder"],
    "Vue": ["price-tracker", "pando"],
    "HTML": ["text-editor-engine", "resume-builder"],
    "CSS": ["resume-builder"],
    "Tailwind CSS": ["resume-builder"],
    "Node.js": ["satchat", "text-editor-engine", "pando"],
    "Laravel": ["price-tracker", "custom-order-builder"],
    "REST APIs": ["satchat"],
    "Express.js": ["satchat"],
    "Socket.IO": ["satchat", "text-editor-engine"],
    "PostgreSQL": ["satchat"],
    "MySQL": ["price-tracker", "custom-order-builder"],
    "MongoDB": ["pando"],
    "Prisma ORM": ["satchat"],
    "Redis": ["satchat"],
    "Docker": ["mock-ai", "satchat"],
    "Docker Compose": ["mock-ai", "satchat"],
    "Linux": ["satchat"],
    "Kubernetes": ["satchat"],
    "Helm": ["satchat"],
    "Jenkins": ["satchat"],
    "Terraform": ["satchat"],
    "Nginx": ["satchat"],
    "AWS": ["satchat"],
    "Oracle Cloud": ["satchat"],
    "System Design (HLD, LLD)": ["satchat"],
    "Distributed Systems": ["satchat"],
    "Database Design": ["satchat"],
    "Data Structures & Algorithms": ["text-editor-engine", "satchat", "leetcode"],
    "LeetCode Guardian (Max Rating 2144)": ["leetcode"],
    "Selenium": ["ecommerce-scraping"],
    "BeautifulSoup": ["ecommerce-scraping"],
    "Puppeteer": ["ecommerce-scraping", "price-tracker"],
    "Browser Automation": ["ecommerce-scraping"],
    "Proxy Management": ["ecommerce-scraping", "price-tracker"],
    "Structured Data Extraction": ["ecommerce-scraping", "price-tracker"],
}

# Competitive programming section (between Work and Experience).
CP = {
    "title": "LeetCode Guardian",
    "lede": ("Guardian is LeetCode's highest contest badge. I reached a max contest rating of 2144, in the top 1% "
             "of contest participants, solving timed algorithm problems against thousands of other programmers."),
    "stats": [
        ("2144", "max contest rating"),
        ("Top 1%", "of contest participants"),
        ("2,100+", "problems solved, all in a public repo"),
    ],
    "where": [
        "<b>SatChat:</b> exponential and binary search over a conversation, so jumping to any search result takes O(log n) one-row queries instead of loading page after page.",
        "<b>Text editor engine:</b> two stacks that meet at the cursor, plus running row totals, so edits and cursor position are O(1) however long the document is.",
        "<b>Pando:</b> a stacking constraint added to a truck-loading optimization engine while keeping its existing optimization behavior.",
        "<b>Price tracker:</b> daily, 30-day and all-time lows and sale runs worked out from every stored price snapshot.",
    ],
    "tool": ("I also built my own practice setup: a Chrome extension, a local Python daemon and a Neovim plugin "
             "that open any LeetCode problem in Neovim as a ready-to-run file."),
    "links": [
        ("LeetCode profile", "leetcode"),
        ("Solutions on GitHub", "https://github.com/Sathishr424/LeetcodeProblems"),
        ("Neovim companion", "https://github.com/Sathishr424/LeetcodeCompanion"),
    ],
}
