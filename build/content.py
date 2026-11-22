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
    "upwork": "https://www.upwork.com/freelancers/~01b87d2baf21208fc5",
    "resume_pdf": "Sathish-Kumar-Resume.pdf",
    "resume_source": "/home/sathish/Documents/Sathish Resume 21th Nov 2026.pdf",
    "headline": "I build web apps, real‑time systems and the data pipelines behind them.",
    "intro": (
        "Full stack engineer with 5 years of experience and 90+ client projects shipped as a "
        "Top Rated freelancer on Upwork. I work across Python, Node.js and Laravel backends and "
        "React and Vue frontends, and I like the hard parts: real-time voice and chat, editors "
        "built from scratch, and scrapers that get through bot protection."
    ),
    "meta_description": (
        "Sathish Kumar, full stack software engineer in Chennai. Case studies: a real-time voice "
        "AI interviewer, a scalable chat platform, a canvas text editor engine, and client work "
        "in scraping and e-commerce."
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
        ("2144", "LeetCode rating, top 1%"),
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
        "where": "Cistron Infotek & Moldtek Technologies · Chennai",
        "points": [
            "Produced structural steel erection and shop drawings in Tekla Structures, following project specifications and applicable engineering standards.",
        ],
    },
]

SKILLS = [
    # Copied from "Sathish Resume 21th Nov 2026.pdf". Keep these in sync with the resume.
    ("Languages", ["JavaScript", "TypeScript", "Python", "Java", "C/C++", "PHP", "SQL", "Bash"]),
    ("AI & LLM Engineering", ["LLM API Integration", "Claude SDK", "Tool/Function Calling", "Model Context Protocol (MCP)",
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
        "facts": [("Role", "Sole developer"), ("Time to first audio", "3–5 seconds"), ("Tests", "800+ automated")],
        "links": [],
        "link_note": "Code walkthrough and demo available on request.",
        "body": [
            ("h", "The problem"),
            ("p", "Reading interview questions is easy. Answering them out loud, under a little pressure, is not. "
                  "Most practice tools are text chat, and they never show you <i>how</i> your answer could have been better."),
            ("h", "What I built"),
            ("p", "Mock AI runs three kinds of interview: a recruiter call, a technical round (you pick the role, level, skills "
                  "and difficulty) and a behavioural round. The interviewer asks one question at a time, follows up when an "
                  "answer is vague, and lets you talk over it. When it ends you get:"),
            ("ul", ["a score out of 100 and a mark out of 10 for each of the round's criteria",
                    "strengths, what to work on, and feedback under every answer in the transcript",
                    "a stronger rewrite of one of your answers",
                    "a recording of both voices, long pauses trimmed, that you can replay from any line or download"]),
            ("img", "mockai/06-report-score-and-criteria.png", "The report: overall score, summary and per-criterion marks."),
            ("h", "How it works"),
            ("p", "Audio streams over a single FastAPI WebSocket through voice detection, speech-to-text, the LLM interviewer "
                  "and text-to-speech. Replies are spoken sentence by sentence as they're generated, so the first audio "
                  "arrives in 3–5 seconds. Each stage sits behind an interface, so the same app runs fully local on a 6 GB GPU "
                  "(Whisper, Chatterbox, Ollama) or on cloud APIs (Cartesia, Ollama Cloud) by changing configuration."),
            ("h", "The hard parts"),
            ("ul", ["<b>Turn-taking.</b> Telling when someone has finished speaking, not just paused to think, without cutting them off.",
                    "<b>Interruptions.</b> When you speak over the interviewer, playback stops, and the conversation only keeps what you actually heard.",
                    "<b>The recording.</b> Merging both voices into one timeline, trimming the thinking gaps, and linking each transcript line to its point in the audio. Audio never leaves the browser.",
                    "<b>Useful scores from a small model.</b> Schema-validated JSON with one retry and per-round criteria on the server. In testing, strong interviews scored 75–88 and weak ones 13–20."]),
            ("img", "mockai/09-transcript-with-recording.png", "The transcript with the recording and per-answer feedback."),
            ("h", "Engineering"),
            ("ul", ["Built test-first: about 560 backend tests, 187 client unit tests and 92 Playwright end-to-end tests, including accessibility checks",
                    "A stub mode so the test suite runs without any models, plus smoke tests against real ones",
                    "Multi-stage Docker builds and Compose profiles for the local-GPU and cloud setups"]),
        ],
    },
    # ------------------------------------------------------------------ SatChat
    {
        "slug": "satchat",
        "title": "SatChat",
        "tagline": "A real-time chat platform built to scale out, with presence, read receipts, files and GIFs, deployed on Kubernetes.",
        "kind": "Personal project", "kind_key": "personal", "year": "2026", "featured": True,
        "cover": "satchat/cover-upwork.png",
        "tags": ["React", "TypeScript", "Node.js", "Socket.IO", "Redis", "PostgreSQL", "Kubernetes", "Jenkins"],
        "skills": ["React", "TypeScript", "Node.js", "WebSockets", "Redis", "Docker", "Kubernetes"],
        "facts": [("Role", "Sole developer"), ("Services", "7 containers behind Nginx"), ("Deploy", "Docker Compose or Kubernetes")],
        "links": [("Live demo", "https://satdevopsdummies.xyz/"), ("Source on GitHub", "https://github.com/Sathishr424/ChatApp_plus_devops")],
        "body": [
            ("h", "What it is"),
            ("p", "A simplified Slack or Discord: one-to-one chats and group channels with live delivery, presence, typing "
                  "indicators, read receipts, file sharing, GIFs, message search and email alerts. It works on desktop and mobile."),
            ("img", "satchat/realtime-details.png", "The details that make chat feel live."),
            ("h", "How it's built"),
            ("img", "satchat/architecture.png", "Seven containers, four written for this project, behind Nginx."),
            ("ul", ["<b>Separate REST and WebSocket tiers.</b> REST is stateless and easy to scale; socket connections are long-lived and scale differently. Both share one domain codebase.",
                    "<b>Redis to scale sockets horizontally.</b> Any socket server can emit to a room, and Redis pub/sub relays it to whichever server holds the recipient's connection.",
                    "<b>Presence that survives many tabs.</b> Each user has a set of live socket IDs in Redis; they go offline only when the last one disconnects, and only that final disconnect writes \"last seen\" to Postgres.",
                    "<b>Persist, then broadcast.</b> A message is saved before anyone hears about it, so the database defines the order.",
                    "<b>Unread counts stored, not counted.</b> Sending increments a counter and opening the chat resets it, so the sidebar never counts rows.",
                    "<b>Build once, deploy anywhere.</b> The client reads its URLs at container start, so one image runs in every environment."]),
            ("img", "satchat/presence-across-devices.png", "Presence stays correct across tabs and devices."),
            ("h", "Shipping it"),
            ("ul", ["Docker Compose for the full stack locally or on one VM",
                    "Helm charts per component, with autoscaling for the API, socket, storage and client tiers",
                    "Jenkins pipelines that build and push images, then deploy to a VM or a Kubernetes cluster provisioned with Terraform",
                    "<code>/health</code> and <code>/ready</code> checks on every service, Nginx with SSL in front"]),
            ("img", "satchat/features-mobile.png", "On mobile."),
        ],
    },
    # ------------------------------------------------------------------ Text editor
    {
        "slug": "text-editor-engine",
        "title": "Text Editor Engine",
        "tagline": "A multi-page document editor built from scratch on HTML Canvas, with its own text model, layout, cursor and undo.",
        "kind": "Personal project", "kind_key": "personal", "year": "2025",
        "cover": "text-editor-engine/01-cover.png",
        "tags": ["TypeScript", "HTML Canvas", "Data structures", "Dependency injection", "Pub/sub"],
        "skills": ["TypeScript", "Canvas"],
        "facts": [("Role", "Sole developer"), ("Core libraries", "None"), ("Next", "Real-time collaboration")],
        "links": [("Source on GitHub", "https://github.com/Sathishr424/DistributedRealTimeCollaborativeDocumentEditor")],
        "body": [
            ("h", "Why build it"),
            ("p", "Most web editors sit on <code>contenteditable</code> or a library like ProseMirror. I wanted to understand what "
                  "those hide, so I wrote every layer myself: how text is stored, how it becomes lines and pages, how it's painted, "
                  "and how the cursor, selection and undo stay consistent through all of it."),
            ("h", "What it does"),
            ("ul", ["<b>Multi-page documents.</b> Text flows onto new pages as you type and empty pages disappear. Each page is its own canvas, and clicks map back to the right page and position.",
                    "<b>Cursor and selection.</b> Arrow keys, Shift and Ctrl combinations, word, line and drag selection, across wrapped lines and page breaks.",
                    "<b>Undo and redo.</b> Every edit is an insert or delete operation on a history stack. Continuous typing merges into one step, and undo restores the cursor too.",
                    "<b>Commands.</b> Keyboard input goes through a command registry, so shortcuts can be rebound."]),
            ("h", "Architecture"),
            ("img", "text-editor-engine/02-architecture.png", "Input flows one way; the renderer only listens for events."),
            ("p", "Keyboard and mouse go to an input controller, then a command registry, then a document service that coordinates "
                  "the text model, cursor, history and layout. Those publish events, and the renderer listens. Nothing calls the "
                  "renderer directly, so each part can be tested and replaced on its own, and subsystems are passed in by dependency injection."),
            ("h", "The text model"),
            ("img", "text-editor-engine/03-text-model-and-undo.png", "A linked list backed by a custom deque, with operation-based undo."),
            ("p", "Text lives in a doubly linked list backed by a custom deque. Typing at the cursor relinks two neighbouring nodes "
                  "instead of shifting an array, so an edit near the cursor costs the same however long the document is."),
            ("h", "Lazy rendering"),
            ("img", "text-editor-engine/04-lazy-rendering.png", "Only the region an edit touched is repainted."),
            ("p", "An edit marks only the affected region of one page for repainting, so typing stays fast as documents grow."),
            ("h", "Next"),
            ("p", "Real-time collaboration: a server that orders and transforms operations (OT, or a sequence CRDT), shared cursors, "
                  "per-user undo and merging offline edits."),
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
        "facts": [("Role", "Sole developer"), ("Templates", "4, more on the way"), ("Section types", "15")],
        "links": [],
        "link_note": "Code walkthrough available on request.",
        "body": [
            ("h", "The problem"),
            ("p", "Most resume builders hide the PDF behind a sign-up, or show the result only after you finish the form. "
                  "I wanted one where you see the real page while you type and can download it straight away, with no account."),
            ("h", "What it does"),
            ("ul", ["<b>Editor</b> for 15 section types: employment, education, projects, skills with a level slider, languages, links, certificates, custom sections and more. Sections and the entries inside them can be dragged into order, renamed and deleted.",
                    "<b>Live preview</b> of an A4 page beside the form, scaled to fit, in one of four templates.",
                    "<b>PDF export</b> through an A4 print window with margins repeated on every page, so long resumes break cleanly.",
                    "<b>Autosave</b> to local storage a second after you stop typing, plus JSON export and import.",
                    "<b>Phones</b> get Edit and Preview tabs, and there's a light and dark theme."]),
            ("img", "resume-builder/light/editing.png", "The form and the A4 page stay in sync."),
            ("h", "Templates are pluggable"),
            ("img", "resume-builder/light/templates.png", "Four templates, one set of data."),
            ("p", "Each template is a single React component file. Adding one means creating the file and registering it in the "
                  "template list; it then appears in the gallery and renders the same resume data. More templates are on the way."),
            ("h", "How it's built"),
            ("img", "resume-builder/light/how-it-works.png", "Plain TypeScript classes; React only renders templates to static HTML."),
            ("p", "There's no UI framework. Each section is a TypeScript class on a shared <code>Draggable</code> base that handles the "
                  "drag handle, drop placeholder, reordering and delete. Every edit notifies a pub/sub manager that debounces to one "
                  "refresh a second after typing stops; the store saves the resume as JSON and the preview re-renders the chosen "
                  "template with React's <code>renderToStaticMarkup</code>. A small router serves the gallery, the builder and a 404 page."),
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
        "facts": [("Stores", "51"), ("Products", "300k+"), ("Largest store", "77k+ products")],
        "links": [],
        "body": [
            ("h", "The problem"),
            ("p", "Retailers, resellers and catalog teams needed product data from other stores: whole catalogs with prices, specs "
                  "and images, in a format they could import. Copying it by hand would take months, and every site is built differently."),
            ("h", "What I built"),
            ("p", "A custom Python scraper for each store:"),
            ("ul", ["<b>Finding products</b> by walking category pages or sitemaps, or from the client's own URL or SKU list.",
                    "<b>Fetching pages</b> with Requests and BeautifulSoup for static sites, and Selenium with undetected Chrome for dynamic sites, infinite scroll, reCAPTCHA and heavily protected stores. Threads, proxies and rotating user agents kept big runs fast, and failed URLs were logged and retried.",
                    "<b>Extracting fields:</b> titles, SKUs, brands, categories, prices, sale prices and rebates, options, stock, shipping, specs as clean HTML, manuals, videos and images.",
                    "<b>Delivering</b> CSV or Excel files in the client's column format, with images downloaded and named to match."]),
            ("img", "scraping/stores-scraped.png", "51 stores, up to 77k+ products from one."),
            ("h", "Scale"),
            ("p", "The largest jobs were 77k+ products from one tools retailer, 56k+ and 38k+ from others, and 140k+ product URLs "
                  "crawled on a single site. The smallest were brand sites with under 100 products."),
            ("img", "scraping/sample-outputs.png", "Real output files, first rows only."),
            ("img", "scraping/how-it-works.png", "The pipeline, the fields delivered and the toolkit."),
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
