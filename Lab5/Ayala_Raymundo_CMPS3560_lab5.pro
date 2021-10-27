/*Lab 5 Media Advisor
- Modified by: Raymundo Ayala 10/20/2021 */
go :-
    hypothesize(Medium),
    write('The training medium suggested is: '),
    write(Medium),
    nl ,
    undo .

/* Hypotheses to be tested */
hypothesize(role_play) :- medium(role_play), !.
hypothesize(lecture) :- medium(lecture), !.
hypothesize(videocasette) :- medium(videocasette), !.
hypothesize(workshop) :- medium(workshop), !.
hypothesize(unknown) .

/* environment rules */
stimulus_situation(verbal) :- 
    verify(environment_papers);
    verify(environment_manuals);
    verify(environment_documents);
    verify(environment_textbooks) .
stimulus_situation(visual) :- 
    verify(environment_pictures);
    verify(environment_illustrations);
    verify(environment_photographs);
    verify(environment_diagrams) .
stimulus_situation(physical_object) :- 
    verify(environment_machines);
    verify(environment_buildings);
    verify(environment_tools) .
stimulus_situation(symbolic) :- 
    verify(environment_numbers);
    verify(environment_formulas);
    verify(environment_computer_programs) .
stimulus_response(oral) :- 
    verify(job_lecture);
    verify(job_advising);
    verify(job_counseling) .
stimulus_response(hands_on) :-
    verify(job_building);
    verify(job_repairing);
    verify(job_troubleshooting) .
stimulus_response(documented) :-
    verify(job_writing);
    verify(job_typing);
    verify(job_drawing) .
stimulus_response(analytical) :-
    verify(job_evaluating);
    verify(job_reasoning);
    verify(job_investigation) .

/* Medium identification rules */

medium(workshop) :-
    stimulus_situation(physical_object),
    stimulus_response(hands_on),
    verify(feedback_required) .
medium(lecture) :-
    stimulus_situation(visual),
    stimulus_response(analytical),
    verify(feedback_required) .
medium(videocasette) :-
    stimulus_situation(visual),
    stimulus_response(documented),
    verify(feedback_not_required) .
medium(lecture) :-
    stimulus_situation(visual),
    stimulus_response(oral),
    verify(feedback_required), !.
medium(lecture) :-
    stimulus_situation(verbal),
    stimulus_response(analytical),
    verify(feedback_required) .
medium(role_play) :-
    stimulus_situation(verbal),
    stimulus_response(oral),
    verify(feedback_required) .

    /* dynamic variables */

    :- dynamic(environment/1) .
    :- dynamic(job/1) .
    :- dynamic(feedback/1) .

    /* User interface for asking questions and receving 
    Response */
    /* Asserts -----> "environment(ex)" */
    ask(Question) :-
    write('Is  '),
    write(Question),
    write('? '),
    write( ': '),
    read(Response),
    nl,
    ( (Response == yes ; Response == y) 
        ->
        assert(yes(Question)) ;
        assert(no(Question)), fail
     ) . 



/* Verifying if 'S' exists */
:- dynamic(yes/1) .
:-dynamic(no/1) .
verify(S) :-
    (
        yes(S) -> true ;
        (no(S) -> fail ; ask(S)) 
    ).
undo :- retract(environment(_)) , fail .
undo :- retract(job(_)), fail .
undo :- retract(feedback(_)), fail .
undo :- retract(yes(_)), fail .
undo :- retract(no(_)), fail.
undo .



