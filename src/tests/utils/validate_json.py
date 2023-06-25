def validate_json(json_data, expected_json, is_validate_values=False):
    # Validate all keys and values in json_data

    # Recorre las claves esperadas en el JSON
    for key in expected_json:
        # Comprueba si la clave está presente en el JSON de entrada
        if key not in json_data:
            return False

        # Get the expected value for the key
        expected_value = expected_json[key]

        # Get the actual value from the JSON data
        actual_value = json_data[key]

        # Comprueba si el valor es un diccionario recursivamente
        if isinstance(expected_value, dict):
            if not isinstance(actual_value, dict):
                return False
            # Valida el diccionario interno recursivamente
            if not validate_json(actual_value, expected_value):
                return False

        if is_validate_values:
            if actual_value != expected_value:
                return False

    return True