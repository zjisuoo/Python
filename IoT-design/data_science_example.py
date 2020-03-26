def do_report(data_source) :
    # fetch and prepare data
    data = fetch_data(data_source)
    parsed_data = parse_data(data
    filtered_data = filtered_data(parsed_data)
    polished_data = polished_data(filtered_data)

    # run algorithms on data
    final_data = analyse(polished_data)

    # create and return report
    report = Report(final_data)
    return report