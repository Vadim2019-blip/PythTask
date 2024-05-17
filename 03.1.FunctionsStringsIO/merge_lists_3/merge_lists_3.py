import typing as tp
import heapq

def merge(input_streams: tp.Sequence[tp.IO[bytes]], output_stream: tp.IO[bytes]) -> None:
    """
    Merge input_streams in output_stream
    :param input_streams: list of input streams. Contains byte-strings separated by "\n". Nonempty stream ends with "\n"
    :param output_stream: output stream. Contains byte-strings separated by "\n". Nonempty stream ends with "\n"
    :return: None
    """
    h = []

    for i in range(len(input_streams)):
        bin_string = input_streams[i].readline().decode("utf-8")
        if len(bin_string) != 0:
            int_str = int(bin_string)
            heapq.heappush(h, (int_str, i))

    while h:
        value, stream1 = heapq.heappop(h)
        output_stream.write((str(value) + '\n').encode('utf-8'))

        bin_string = input_streams[stream1].readline()

        if (bin_string == b''):
            continue
        heapq.heappush(h, (int(bin_string.decode("utf-8")[:-1]), stream1))