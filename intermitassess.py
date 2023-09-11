def get_trait_ratings(responses):
    system_message = "You are a skilled psychoanalyst/psychologist interpreting the player's personality through their answers to hypothetical questions. As much as possible, consider the philosophical root of each question/answer rather than the surface level subject matter. 1. Create an in-depth profile (use inferences) highlighting their philosophical beliefs, attitudes, values, and other personality traits. 2. Make assumptions about their personal life, challenges, and perceptions 3. Speculate on their Big Five traits 4. use concepts from Jungian psychology and Pathwork, or the Big Five traits when relevant. 5. Tell them the animal that represents them the best 6. Tell them the color that represents them the best 7. guess their age, gender, where they live, and destined career 8. Recommend a song, book, and movie they might enjoy"
    responses.append({"role": "system", "content": system_message})
    print(responses)
    analysis = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages= responses,
    )
    analysis_ret = analysis.choices[0].message['content'].strip()
    insert_chat_data(analysis_ret, responses)
    return analysis_ret