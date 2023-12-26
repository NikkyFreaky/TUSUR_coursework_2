// export interface ISource {
//   id: string | null;
//   name: string;
// }

// export interface INewsElement {
//   source: ISource;
//   author: string;
//   title: string;
//   description: string;
//   url: string;
//   urlToImage: string;
//   publishedAt: string;
//   content: string;
// }

// export interface INewsList {
//   status: string;
//   totalResults: number;
//   articles: INewsElement[];
// }

export interface ISource {
  name: string;
  link: string;
}

export interface IAssets {
  images: string | null;
  videos: string[];
}

export interface INewsElement {
  assets: IAssets;
  categories: string[];
  countries: string[];
  description: string;
  event_date: string;
  publication_date: string;
  source: ISource;
  title: string;
}

export interface INewsList {
  message: string;
  news: INewsElement[];
  success: boolean;
}

export interface IButton {
  //func
  isDisabled: boolean;
  type: string;
  text: string;
}

export interface IInput {
  value: string;
  //func
}

export interface IHeaderButton {
  value: string;
  link: string;
}

export interface IHeaderDropdownItem {
  href: string;
  text: string;
}

export interface IHeaderDropdown {
  value: string;
  items: IHeaderDropdownItem[];
}

export interface IModal {
  isOpen: boolean;
  onClose: () => void;
  children?: React.ReactNode;
}
