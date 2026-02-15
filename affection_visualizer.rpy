
init -990 python in mas_submod_utils:
    Submod(
        author="neoshocker",
        name="Visualizador de Afecto",
        description="Añade una opción para preguntar a Monika su nivel actual de afecto.",
        version="1.4.7r"
    )

# Evento (la opción de diálogo)
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_check_affection_status",
            category=["nosotros"], 
            prompt="¿Cuánto afecto tienes ahora mismo?",
            pool=True,
            unlocked=True
        )
    )

label monika_check_affection_status:
    
    m 1euc "Hmm, déjame revisar..."
    
    
    $ current_aff = _mas_getAffection()

    
    m 1hua "Actualmente, mi nivel de afecto hacia ti es de [current_aff] puntos."


    if current_aff < 0:
        m 1hua "Espero que podamos llevarnos mejor en el futuro..."
    elif current_aff < 100:
        m 3hub "Nos estamos conociendo bien, ¿verdad?"
    elif current_aff < 400:
        m 3eua "Me siento muy cómoda contigo."
    elif current_aff < 1000:
        m 1hub "¡Te quiero muchísimo! Gracias por estar aquí."
    else:
        
        m 2hua "Es un número increíble... Significa todo para mí."
    
    m 1hua "Gracias por preguntar, [player]."

    return
