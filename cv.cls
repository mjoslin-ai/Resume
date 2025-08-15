%---------------------------------------------------------------
%	CLASS CONFIGURATION
%---------------------------------------------------------------

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{cv}

\DeclareOption*{\PassOptionsToClass{\CurrentOption}{extarticle}} % Pass through any options to the base class
\ProcessOptions\relax % Process given options

\LoadClass{extarticle} % Load the base class

%---------------------------------------------------------------
%	PACKAGES AND OTHER DOCUMENT CONFIGURATIONS
%---------------------------------------------------------------

\setlength{\parindent}{0mm} % Suppress paragraph indentation

\usepackage[hidelinks]{hyperref} % Required for links but hide the default boxes around links

\pagestyle{empty} % No headers or footers

\usepackage{moresize} % Provides more font size commands (\HUGE and \ssmall)
\usepackage{enumitem}

%---------------------------------------------------------------
%	PAGE LAYOUT
%---------------------------------------------------------------

\usepackage{geometry} % Required for adjusting page dimensions and margins

\geometry{
	paper=a4paper, % Paper size, change to letterpaper for US letter size
	top=0.5in, % Top margin
	bottom=0.5in, % Bottom margin
	left=0.5in, % Left margin
	right=0.5in, % Right margin
	%headheight=0.75cm, % Header height
	%footskip=1cm, % Space from the bottom margin to the baseline of the footer
	%headsep=0.5cm, % Space from the top margin to the baseline of the header
	%showframe, % Uncomment to show how the type block is set on the page
}

%---------------------------------------------------------------
%	FONTS
%---------------------------------------------------------------

\usepackage[utf8]{inputenc} % Required for inputting international characters
\usepackage[T1]{fontenc} % Output font encoding for international characters

%\usepackage[default]{raleway}
%\usepackage[defaultsans]{droidsans}
%\usepackage{cmbright}

%\renewcommand*\familydefault{\sfdefault} % Force the sans-serif version of any font used

\usepackage[scaled]{helvet}
\renewcommand*\familydefault{\sfdefault}

%------------------------------------------------

\usepackage{fontawesome5} % Required for FontAwesome icons

% Command to output an icon in a black square box with text to the right
\newcommand{\icon}[3]{% The first parameter is the FontAwesome icon name, the second is the box size and the third is the text
	\vcenteredhbox{\colorbox{white}{\makebox(#2, #2){\textcolor{black}{\Large\csname fa#1\endcsname}}}}% Icon and box
	\hspace{0.1cm}% Whitespace
	\vcenteredhbox{\textcolor{black}{#3}}% Text
}

%---------------------------------------------------------------
%	GRAPHICS DEFINITIONS
%---------------------------------------------------------------

\usepackage{tikz} % Required for creating the plots
\usetikzlibrary{shapes, backgrounds}
\tikzset{x=1cm, y=1cm} % Default tikz units

% Command to vertically centre adjacent content
\newcommand{\vcenteredhbox}[1]{% The only parameter is for the content to centre
	\begingroup%
		\setbox0=\hbox{#1}\parbox{\wd0}{\box0}%
	\endgroup%
}

%---------------------------------------------------------------
%	CUSTOM SECTIONS
%---------------------------------------------------------------

\def\Vhrulefill{\leavevmode\leaders\hrule height 0.7ex depth \dimexpr0.4pt-0.7ex\hfill\kern0pt}

% Command to output section title headings
\newcommand{\cvsect}[1]{% The only parameter is the section text
	\vspace{\baselineskip} % Whitespace before the section title
	\textcolor{black}{ \MakeUppercase{\textbf{#1}}} \hspace{4pt} \Vhrulefill \\% Section title
}

%---------------------------------------------------------------
%	ENTRY LIST
%---------------------------------------------------------------

\usepackage{longtable} % Required for tables that span multiple pages
\setlength{\LTpre}{0pt} % Remove default whitespace before longtable
\setlength{\LTpost}{0pt} % Remove default whitespace after longtable

\setlength{\tabcolsep}{0pt} % No spacing between table columns

% Environment to hold a new list of entries
\newenvironment{entrylist}{
	\begin{longtable}[H]{l l}
}{
	\end{longtable}
}

\newcommand{\entry}[4]{% First argument for the leftmost date(s) text, second is for the bold entry heading, third is for the bold right-aligned entry qualifier and the fourth is for the entry description
	\parbox[t]{0.18\textwidth}{% 17.5% of the text width of the page
	   \small #1 % Leftmost entry date(s) text
	}%
	&\parbox[t]{0.82\textwidth}{% 82.5% of the text width of the page
		\textbf{#2}% Entry heading text
		\ifx#3\empty\else
			\hfill% Horizontal whitespace
			{\footnotesize \textbf{\textcolor{black}{#3}}}% Right-aligned entry qualifier text
		\fi
		\ifx#4\empty\else
			\\#4 % Entry description text
		\fi
	}\\\\}

% Command to output a separator slash between lists, e.g. '  /  '
\newcommand{\slashsep}{\hspace{3mm}/\hspace{3mm}}

%---------------------------------------------------------------
%	FUNCTIONS
%---------------------------------------------------------------

\newcommand{\cvHeader}[6]{%
    \begin{center}
        \parbox[t]{0.95\textwidth}{%
            \centering
            \vspace{-\baselineskip} % Adjust vertical alignment
            {\fontsize{16}{20} \textcolor{black}{\textbf{\MakeUppercase{#1}}}} \\ % Name on its own row
            \vspace{6pt} % Space below name
            {#2 \ | \ #3} \\ % Phone and location on their own row
            \vspace{6pt} % Space below phone and location
            {\href{mailto:#4}{#4} \ | \ \href{https://#5}{#5} \ | \ \href{https://www.#6}{#6}} % Email, GitHub, LinkedIn on their own row
        }
    \end{center}
}


\newcommand{\cvEntry}[5]{%
    \entry{#1\
        \ifx#2\empty % Handles missing end date
        \else -- #2%
        \fi
    }
    {#3} % Title
    {#4} % Source/Company
    {\vspace{-10pt}%
    \ifx#5\empty
    \else    
        {\expandafter\begin{itemize}[noitemsep,topsep=0pt,parsep=0pt,partopsep=0pt, leftmargin=-1pt]
            #5
        \end{itemize}}
    \fi
    }
}


\newcommand{\cvRef}[4]{
    \vspace{\baselineskip}
    \vspace{-10 pt}
    \textbf{#1}\\
    #2\\
    \icon{Envelope}{11}{#3}\\
    \icon{Phone}{11}{#4}\\
}